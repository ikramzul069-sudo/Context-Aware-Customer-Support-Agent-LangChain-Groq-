# Context-Aware Customer Support Agent (LangChain & Groq)

<div align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Framework-LangChain-green.svg" alt="LangChain">
  <img src="https://img.shields.io/badge/API-Groq-orange.svg" alt="Groq">
</div>

---

## 1. About This Project & File Structure

### Project Description
This project implements a context-aware Customer Support Agent using Python, LangChain, and the Groq API. 

The primary objective of this project is to demonstrate how to build an AI agent capable of retaining conversational memory. The agent leverages the `llama-3.1-8b-instant` model to act as a friendly and helpful customer service representative. By utilizing LangChain's `RunnableWithMessageHistory` and `InMemoryChatMessageHistory`, the agent effectively tracks the session state, allowing it to remember past interactions and provide highly contextual, relevant responses to follow-up questions (e.g., handling product complaints and warranty claims).

### File Structure & Functionality
Here is a breakdown of what each file in this repository does:
* **`app.py`** : The main Python script containing the complete conversational pipeline. It initializes the ChatGroq model, defines the system prompt and memory placeholders, wraps the chain with a session-based chat history, and runs a simulated terminal-based chat to test the agent's memory retention.

---

## 2. Set-Up
Before running this project, ensure your local environment has the following dependencies installed:

1. **Python:** Python 3.x installed on your system.
2. **Groq API Key:** You must have a valid API key from Groq. Set it as an environment variable on your machine (`export GROQ_API_KEY="your_api_key_here"`).
3. **Python Libraries:** Install the required LangChain and Groq packages using `pip`:
```bash
pip install langchain-core langchain-groq
```
## 3. Compilation
Since this project uses Python, traditional compilation (like make or gcc) is not required. Instead, you need to use the Python interpreter to execute the script directly.

Ensure that your app.py file is saved in your directory and your environment variables are configured.

## 4. Execution
You run this conversational simulation directly from the command line.
Running the Script:
Open your terminal in the project directory and execute the script:

```Bash
python app.py
```

Expected Results:
Once the script executes, you will see a simulated text conversation in your terminal.

The first interaction will show the AI acknowledging the broken screen issue.

In the second interaction, the AI will successfully combine the context of the broken screen from the first message with the new information (Samsung brand and warranty question), proving that the conversational memory is fully functional.
