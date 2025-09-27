from app.utils.memory import add_chat, get_recent_chats

def add_chat_history(user, answer):
    add_chat(user, answer)

def get_chat_history():
    return get_recent_chats()
