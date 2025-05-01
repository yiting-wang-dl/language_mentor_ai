from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    """
    Retrieve the chat history for the specified session ID. If the session ID does not exist, a new chat history instance will be created.

    Args:
        session_id (str): Unique identifier for the session.

    Returns:
        BaseChatMessageHistory: Chat history object for the corresponding session
    """
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]