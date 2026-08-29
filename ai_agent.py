from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
import os

from tools import get_cricket_score, get_football_score

load_dotenv()

gemini_key = os.getenv("gemini_key")

if not gemini_key:
    raise RuntimeError("gemini_key not found in .env file")  # ✅ INDENTED

model = init_chat_model(
    "google_genai:gemini-3.6-flash",
    api_key=gemini_key
)

agent = create_agent(
    model=model,
    tools=[
        get_cricket_score,
        get_football_score
    ],
    checkpointer=InMemorySaver(),
    system_prompt=(
        "You are a helpful AI assistant. "
        "Use the cricket score and football score tools when asked. "
        "Use get_cricket_score when the user asks for a cricket score "
        "between India and another country. "
        "Use get_football_score when the user asks for a football score "
        "between two teams."
    )
)

config = {
    "configurable": {
        "thread_id": "1"
    }
}

def main():
    print("AI Agent is ready!")
    print("Type exit or quit to stop.")
    
    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Goodbye!")
            break

        if not user_input:
            continue

        try:
            response = agent.invoke(
                {
                    "messages": [
                        ("user", user_input)
                    ]
                },
                config
            )

            content = response["messages"][-1].content
            print("Agent:", content)

        except Exception as e:
            print("Agent Error:", e)

if __name__ == "__main__":  # ✅ Fixed: double underscores
    main()