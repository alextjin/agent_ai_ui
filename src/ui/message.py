import streamlit as st

from src.models.chat import ChatMessage


ROLE_LABELS = {
    "assistant": "Assistant",
    "user": "You",
}


def render_message(message: ChatMessage) -> None:
    with st.chat_message(message.role):
        label = ROLE_LABELS.get(message.role, message.role.title())
        st.markdown(f'<div class="message-meta">{label}</div>', unsafe_allow_html=True)
        st.markdown(message.content)
