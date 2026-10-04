import logging

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from .config import TELEGRAM_BOT_TOKEN
from .handlers import help_command, message_handler, reset, start

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("IslamicQABot")

def build_application():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("reset", reset))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)
    )
    return app

def main():
    logger.info("Islamic Q&A Bot is starting...")
    app = build_application()
    app.run_polling(
        allowed_updates=["message"],
        drop_pending_updates=True,
    )

if __name__ == "__main__":
    main()
