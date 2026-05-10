import streamlit as st

from src.models.chat import ChatMessage


MESSAGES_KEY = "messages"

WELCOME_MESSAGE = ChatMessage(
    role="assistant",
    content=(
        "Hi, I am your AI assistant. This frontend is ready to connect to a "
        "backend chat API when one is available."
    ),
)


def initialize_chat_session() -> None:
    if not _has_valid_messages():
        st.session_state[MESSAGES_KEY] = [WELCOME_MESSAGE]


def get_messages() -> list[ChatMessage]:
    initialize_chat_session()
    return st.session_state[MESSAGES_KEY]


def add_message(role: str, content: str) -> None:
    messages = get_messages()
    messages.append(ChatMessage(role=role, content=content))


def add_user_message(content: str) -> None:
    add_message(role="user", content=content)


def add_assistant_message(content: str) -> None:
    add_message(role="assistant", content=content)


def reset_chat_session() -> None:
    st.session_state[MESSAGES_KEY] = [WELCOME_MESSAGE]


def _has_valid_messages() -> bool:
    messages = st.session_state.get(MESSAGES_KEY)
    return bool(messages) and isinstance(messages, list) and all(
        isinstance(message, ChatMessage) for message in messages
    )
