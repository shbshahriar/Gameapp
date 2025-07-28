import os
from fastapi import FastAPI, Request
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool, AgentExecutor, create_tool_calling_agent
from langchain_community.tools.tavily_search.tool import TavilySearchResults
import uuid

load_dotenv()

# 🌐 FastAPI Setup
app = FastAPI()

# ✅ CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📩 Request Body
class ChatRequest(BaseModel):
    input: str

# 🤖 LLM Setup
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.7)

# 🔎 Web Search Tool
search_tool_instance = TavilySearchResults()
search_tool = Tool(
    name="web-search",
    func=search_tool_instance.run,
    description="Search the web for recent information."
)

# 🧠 Memory Store (Per User)
user_memories = {}

# 💬 Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You're a helpful AI assistant. Be concise and informative."),
    MessagesPlaceholder(variable_name="chat_history"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
    ("human", "{input}")
])

# 🛠️ Agent
agent = create_tool_calling_agent(llm=llm, tools=[search_tool], prompt=prompt)

# ⚙️ Executor
def get_agent_executor(user_id):
    if user_id not in user_memories:
        user_memories[user_id] = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    memory = user_memories[user_id]
    
    return AgentExecutor(agent=agent, tools=[search_tool], memory=memory, verbose=False)

# 🚪 POST Endpoint
@app.post("/chat")
async def chat(request: ChatRequest, user_id: str = None):
    if user_id is None:
        user_id = str(uuid.uuid4())  # Generate a unique user_id if not provided
    
    agent_executor = get_agent_executor(user_id)
    
    result = agent_executor.invoke({"input": request.input})
    
    return {"response": result["output"], "user_id": user_id}

# ▶️ Run with: python app.py (optional)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
