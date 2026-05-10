import streamlit as st

from src.ui.components import apply_global_styles, configure_page, render_header
from src.ui.input_bar import render_chat_input
from src.ui.message import render_message
from src.ui.sidebar import render_sidebar
from src.ui.streaming import render_streaming_response
from src.utils.session_state import (
    add_user_message,
    get_messages,
    initialize_chat_session,
)


def render_messages() -> None:
    st.markdown('<div class="chat-shell">', unsafe_allow_html=True)
    for message in get_messages():
        render_message(message)
    st.markdown("</div>", unsafe_allow_html=True)


def render_chat_app() -> None:
    configure_page()
    apply_global_styles()
    initialize_chat_session()

    prompt = render_chat_input()
    if prompt:
        add_user_message(prompt)

    render_sidebar()
    render_header()
    render_messages()

    if prompt:
        render_streaming_response(prompt)
