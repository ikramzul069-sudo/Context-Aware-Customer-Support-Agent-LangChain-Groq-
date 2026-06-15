import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_groq import ChatGroq

# 1. Initialize the Model (Ensure GROQ_API_KEY is in your environment variables)
llm = ChatGroq(
    model="llama-3.1-8b-instant", 
    temperature=0.5
)

# 2. Define the Prompt Structure
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly and helpful Customer Service assistant."),
    ("placeholder", "{chat_history}"),  # Replaces MessagesPlaceholder
    ("human", "{input}")
])

# 3. Create the Main Chain
chain = prompt | llm

# 4. Set Up Memory / Chat History Storage
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 5. Wrap the Chain with Message History
cs_agent = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",          # Must match {input} in prompt
    history_messages_key="chat_history"  # Must match {chat_history} in prompt
)

# --- Conversation Simulation ---
print("--- Chat Started ---\n")

message1 = "Hello, the phone I bought yesterday has lines on the screen right after turning it on."
print(f"User: {message1}")

# Invoking the agent requires dictionary mapping
response1 = cs_agent.invoke(
    {"input": message1},
    config={"configurable": {"session_id": "customer_001"}}
)

print(f"AI: {response1.content}\n")

# Memory Verification: Second message to test if AI remembers the context
message2 = "The brand is Samsung, can I return it directly or claim the warranty?"
print(f"User: {message2}")

response2 = cs_agent.invoke(
    {"input": message2},
    config={"configurable": {"session_id": "customer_001"}}
)

print(f"AI: {response2.content}")