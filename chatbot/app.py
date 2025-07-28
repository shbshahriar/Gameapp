import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool, AgentExecutor, create_tool_calling_agent
from langchain_community.tools.tavily_search.tool import TavilySearchResults

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

# 🧠 Memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

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
agent_executor = AgentExecutor(agent=agent, tools=[search_tool], memory=memory, verbose=False)

# 🚪 POST Endpoint
@app.post("/chat")
async def chat(request: ChatRequest):
    result = agent_executor.invoke({"input": request.input})
    return {"response": result["output"]}

# ▶️ Run with: python app.py (optional)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
