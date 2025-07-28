import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool, AgentExecutor, create_tool_calling_agent
from langchain_community.tools.tavily_search.tool import TavilySearchResults

# LLM setup
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.7)

# Web Search Tool
search_tool_instance = TavilySearchResults()
search_tool = Tool(
    name="web-search",
    func=search_tool_instance.run,
    description="Search the web for recent information."
)

# Memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Prompt Template — includes agent_scratchpad this time!
prompt = ChatPromptTemplate.from_messages([
    ("system", "You're a helpful AI assistant. Be concise and informative."),
    MessagesPlaceholder(variable_name="chat_history"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
    ("human", "{input}")
])

# Agent
agent = create_tool_calling_agent(llm=llm, tools=[search_tool], prompt=prompt)

# Executor with memory
agent_executor = AgentExecutor(agent=agent, tools=[search_tool], memory=memory, verbose=False)

# Chat Loop
while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Bye 👋")
        break

    result = agent_executor.invoke({"input": user_input})
    print("Bot:", result["output"])
