import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from langchain_core.messages import HumanMessage

from ai_agent import agent

load_dotenv()

TOKEN = os.getenv("TELEGRAM_KEY")

if not TOKEN:
    raise RuntimeError("TELEGRAM_KEY not found in .env file")


def extract_text(message):
    content = message.content

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts = []

        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                text = block.get("text", "")

                if text:
                    parts.append(text)

        return "\n".join(parts).strip() or "(no reply)"

    return str(content)


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message or not update.message.text:
        return

    user_text = update.message.text

    try:

        result = await agent.ainvoke(
            {
                "messages": [
                    HumanMessage(content=user_text)
                ]
            },
            config={
                "configurable": {
                    "thread_id": str(update.effective_chat.id)
                }
            }
        )

        answer = extract_text(result["messages"][-1])

        await update.message.reply_text(answer)

    except Exception as e:

        print("Agent error:", e)

        await update.message.reply_text(
            "Sorry, something went wrong."
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle
    )
)


print("Telegram bot is running...")

app.run_polling()
