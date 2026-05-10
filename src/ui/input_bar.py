import streamlit as st


def render_chat_input() -> str | None:
    return st.chat_input("Message the assistant...")
