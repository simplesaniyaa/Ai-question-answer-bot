# 🕌 Islamic Q&A Telegram Bot

An AI-powered Telegram bot for general Islamic questions.

## Features

- Hindi / Roman Hindi / Urdu / Roman Urdu / English
- Qur'an, Hadith, Seerah and general Islamic Q&A
- Conversation context per Telegram user
- `/start`, `/help`, `/reset`
- API keys stored in environment variables
- Ready for Heroku-style worker deployment

## Important

This bot provides general information and is not a mufti or a source of binding fatwas. It is designed to avoid inventing religious references. For personal or sensitive fiqh matters, consult a qualified scholar.

## Local setup

1. Install Python 3.12+.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env`.
4. Put your Telegram BotFather token and OpenAI API key in `.env`.
5. Start:

```bash
python -m bot.main
```

## Heroku

Add these Config Vars:

- `TELEGRAM_BOT_TOKEN`
- `OPENAI_API_KEY`
- `OPENAI_MODEL` = `gpt-5.5`

The `Procfile` starts the worker automatically.

## Security

Never commit `.env` or paste your API key into GitHub source files.
