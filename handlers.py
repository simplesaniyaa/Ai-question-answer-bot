from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from .ai import ask_ai
from .history import add_message, clear_history, get_history

WELCOME = """🤲 Assalamu Alaikum!

Main Islamic Question & Answer AI assistant hoon.

Aap Qur'an, Hadith, Seerah, ibadat aur general Islamic maloomat ke baare mein sawal pooch sakte hain.

⚠️ Important: AI se milne wali information ko binding fatwa na samjhein. Personal ya sensitive fiqhi masail ke liye qualified mufti/scholar se mashwara karein.

Bas apna sawal bhejiye."""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(WELCOME)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "📚 Commands:\n"
        "/start - Bot start karein\n"
        "/help - Help\n"
        "/reset - Chat history clear karein\n\n"
        "Example:\n"
        "• Roze ke faraiz kya hain?\n"
        "• Surah Ikhlas ka matlab kya hai?\n"
        "• Zakat kis par farz hoti hai?"
    )

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    clear_history(update.effective_user.id)
    await update.message.reply_text("🧹 Aapki chat history clear kar di gayi hai.")

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or not update.message.text:
        return

    text = update.message.text.strip()
    if not text:
        return

    user_id = update.effective_user.id
    try:
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id,
            action=ChatAction.TYPING,
        )
        answer = await ask_ai(text, get_history(user_id))
        add_message(user_id, "user", text)
        add_message(user_id, "assistant", answer)

        # Telegram message limit is 4096 characters.
        for i in range(0, len(answer), 4000):
            await update.message.reply_text(answer[i:i + 4000])
    except Exception:
        await update.message.reply_text(
            "😔 Abhi jawab generate nahi ho pa raha. "
            "Thodi der baad dobara try karein."
        )
