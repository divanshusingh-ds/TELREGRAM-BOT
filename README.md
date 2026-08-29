# 🤖 AI Telegram Agent

> A modular AI-powered Telegram assistant built with **Python, LangChain, LangGraph, and Google Gemini**, with tool-calling capabilities and conversation memory.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Agent-green)](https://www.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Memory-orange)](https://www.langchain.com/langgraph)
[![Gemini](https://img.shields.io/badge/Google-Gemini-red?logo=google)](https://ai.google.dev/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?logo=telegram\&logoColor=white)](https://telegram.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Overview

**AI Telegram Agent** is a modular AI assistant that brings a LangChain/LangGraph-powered agent directly into Telegram.

Instead of building a simple chatbot that only generates text, this project demonstrates an **AI agent architecture** where the model can reason about a user's request and interact with external tools when necessary.

The project currently includes a **cricket score tool** as an example of agent tool-calling.

The architecture is designed so additional tools and capabilities can be added without rebuilding the entire application.

---

## ✨ Features

* 🤖 **Google Gemini powered AI**
* 🧠 **LangChain Agent architecture**
* 🔄 **LangGraph conversation checkpointing**
* 🛠️ **Tool calling**
* 🏏 **Cricket score tool**
* 💬 **Telegram integration**
* 🧵 **Conversation/thread-based memory**
* 🔐 **Environment variable based API key management**
* 🧩 **Modular architecture**
* 📦 **Requirements-based dependency management**
* 🚀 Designed for future cloud deployment

---

## 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │      Telegram        │
                    │        User          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       bot.py         │
                    │ Telegram Interface   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    LangChain Agent   │
                    │     ai_agent.py      │
                    └──────────┬───────────┘
                               │
                     ┌─────────┴─────────┐
                     │                   │
                     ▼                   ▼
             ┌───────────────┐   ┌───────────────┐
             │ Google Gemini │   │    Tools      │
             │      LLM      │   │   tools.py    │
             └───────────────┘   └───────┬───────┘
                                         │
                                         ▼
                                ┌─────────────────┐
                                │ Cricket Tool    │
                                │ get_cricket_score│
                                └─────────────────┘

                       ┌──────────────────────┐
                       │  LangGraph Memory    │
                       │   InMemorySaver      │
                       └──────────────────────┘
```

---

## 🔄 How It Works

### 1. User sends a message

The user sends a message through Telegram.

Example:

```text
India vs Australia cricket score
```

### 2. Telegram receives the message

`bot.py` receives the message using `python-telegram-bot`.

### 3. Message is passed to the AI Agent

The message is converted into a LangChain message and sent to the agent.

### 4. Gemini processes the request

Google Gemini acts as the language model behind the agent.

### 5. Agent decides whether a tool is required

For normal conversation:

```text
User → Gemini → Response
```

For tool-based requests:

```text
User
 ↓
Agent
 ↓
Tool
 ↓
Tool Result
 ↓
Agent
 ↓
Response
```

### 6. Response is sent back to Telegram

The final response is returned to the user through Telegram.

---

## 🧠 Why an Agent?

A traditional chatbot generally follows:

```text
Input → LLM → Output
```

This project follows an agent-based architecture:

```text
Input
  ↓
AI Agent
  ↓
Reason about request
  ↓
Choose tool if necessary
  ↓
Execute tool
  ↓
Process result
  ↓
Final response
```

This makes the application easier to extend with new capabilities.

---

## 🛠️ Tech Stack

| Technology          | Purpose                         |
| ------------------- | ------------------------------- |
| Python              | Core programming language       |
| Google Gemini       | Large Language Model            |
| LangChain           | Agent and tool framework        |
| LangGraph           | Agent state and checkpointing   |
| python-telegram-bot | Telegram integration            |
| python-dotenv       | Environment variable management |
| InMemorySaver       | Conversation checkpointing      |

---

## 📂 Project Structure

```text
TELREGRAM-BOT/
│
├── ai_agent.py
│   └── Creates and configures the AI agent
│
├── bot.py
│   └── Telegram bot interface
│
├── tools.py
│   └── Custom tools available to the agent
│
├── requirements.txt
│   └── Python dependencies
│
├── .gitignore
│   └── Prevents secrets and temporary files from being committed
│
└── README.md
    └── Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/divanshusingh-ds/TELREGRAM-BOT.git
```

```bash
cd TELREGRAM-BOT
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
gemini_key=YOUR_GEMINI_API_KEY
TELEGRAM_KEY=YOUR_TELEGRAM_BOT_TOKEN
```

### Get a Gemini API key

Create your Gemini API key through Google AI Studio.

### Create a Telegram bot

Create a bot using Telegram's official BotFather and copy the generated bot token.

> ⚠️ **Never commit your `.env` file or expose your API keys publicly.**

The `.gitignore` file is configured to prevent `.env` from being committed.

---

## ▶️ Running the AI Agent Locally

You can test the agent directly from the terminal:

```bash
python ai_agent.py
```

Example:

```text
AI Agent is ready!

You: hello
Agent: Hello! How can I help you?

You: India vs Australia cricket score
Agent: Score between India and Australia is 120-3
```

---

## 🤖 Running the Telegram Bot

Start the Telegram bot:

```bash
python bot.py
```

You should see:

```text
Telegram bot is running...
```

Open Telegram and send a message to your bot.

Example:

```text
Hello
```

or:

```text
India vs Australia cricket score
```

---

## 🏏 Current Cricket Tool

The project currently contains a demonstration cricket tool:

```python
@tool
def get_cricket_score(country: str) -> str:
    ...
```

The tool demonstrates how an AI agent can call a Python function when a user request requires additional information.

> **Note:** The current implementation uses demonstration data. A future version will connect the tool to a real-time cricket data provider.

---

## 🔮 Future Roadmap

The project is designed to grow beyond a simple Telegram chatbot.

### Phase 1 — Core Agent

* [x] Gemini integration
* [x] LangChain agent
* [x] LangGraph checkpointing
* [x] Custom tools
* [x] Telegram integration

### Phase 2 — Intelligence

* [ ] Real-time cricket API
* [ ] Multiple cricket tools
* [ ] Weather tool
* [ ] Web search tool
* [ ] News tool
* [ ] Calculator tool
* [ ] Better long-term memory
* [ ] Tool error handling

### Phase 3 — Multimodal AI

* [ ] Image understanding
* [ ] Document processing
* [ ] Voice messages
* [ ] Speech-to-text
* [ ] Text-to-speech

### Phase 4 — Production

* [ ] Persistent database
* [ ] User authentication
* [ ] Rate limiting
* [ ] Logging and monitoring
* [ ] Docker support
* [ ] Cloud deployment
* [ ] Production-grade memory

---

## 🧩 Extending the Agent

One of the main goals of this project is modularity.

New capabilities can be implemented as tools.

For example:

```text
tools/
├── cricket.py
├── weather.py
├── calculator.py
├── search.py
└── news.py
```

The agent can then decide which tool is appropriate for a user's request.

This creates a foundation for building a **general-purpose AI assistant** rather than a single-purpose chatbot.

---

## 🔐 Security

This project uses environment variables for sensitive credentials.

Never hard-code credentials like:

```python
gemini_key = "YOUR_SECRET_KEY"
```

Instead:

```python
gemini_key = os.getenv("gemini_key")
```

Keep `.env` local and ensure it is included in `.gitignore`.

---

## 📚 What This Project Demonstrates

This project demonstrates practical implementation of:

* AI agents
* LLM integration
* Tool calling
* Agent state
* Conversation memory
* Telegram bot development
* API integration
* Environment variable management
* Modular Python architecture

It is intended as a learning and experimentation project for building tool-using AI systems.

---

## 🚀 Project Vision

The long-term goal is to evolve this project from a Telegram-based assistant into a **modular personal AI platform** capable of interacting with different tools, APIs, data sources, and applications.

The architecture intentionally separates:

```text
Interface
   ↓
Agent
   ↓
LLM
   ↓
Tools
   ↓
External Services
```

This separation makes the system easier to maintain, test, and extend.

---

## 👨‍💻 Author

**Divanshu Singh**

Built with Python, LangChain, LangGraph and Google Gemini.

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is licensed under the MIT License.
