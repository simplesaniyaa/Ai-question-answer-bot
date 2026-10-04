from openai import AsyncOpenAI
from .config import OPENAI_API_KEY, OPENAI_MODEL
from .prompt import ISLAMIC_SYSTEM_PROMPT

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

async def ask_ai(user_text: str, history: list[dict[str, str]]) -> str:
    messages = []
    for item in history:
        messages.append({
            "role": item["role"],
            "content": item["content"],
        })
    messages.append({"role": "user", "content": user_text})

    response = await client.responses.create(
        model=OPENAI_MODEL,
        instructions=ISLAMIC_SYSTEM_PROMPT,
        input=messages,
        max_output_tokens=900,
    )

    answer = (response.output_text or "").strip()
    if not answer:
        raise RuntimeError("AI returned an empty response.")
    return answer
