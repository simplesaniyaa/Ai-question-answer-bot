from collections import defaultdict, deque
from .config import MAX_HISTORY

_histories: dict[int, deque] = defaultdict(lambda: deque(maxlen=MAX_HISTORY))

def get_history(user_id: int) -> list[dict[str, str]]:
    return list(_histories[user_id])

def add_message(user_id: int, role: str, content: str) -> None:
    _histories[user_id].append({"role": role, "content": content})

def clear_history(user_id: int) -> None:
    _histories.pop(user_id, None)
