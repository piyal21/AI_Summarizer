import collections
from app.config import MAX_CHAT_MEMORY

chat_memory = collections.deque(maxlen=MAX_CHAT_MEMORY)

def add_chat(user, answer):
    chat_memory.appendleft((user, answer))

def get_recent_chats():
    return list(chat_memory)
