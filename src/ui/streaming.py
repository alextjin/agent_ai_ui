import time
from collections.abc import Iterator

import streamlit as st

from src.utils.session_state import add_assistant_message


STREAM_DELAY_SECONDS = 0.025


def render_streaming_response(prompt: str) -> None:
    response = _build_frontend_response(prompt)

    with st.chat_message("assistant"):
        st.markdown('<div class="message-meta">Assistant</div>', unsafe_allow_html=True)
        indicator = st.empty()
        indicator.markdown(
            '<div class="typing-indicator">Assistant is typing...</div>',
            unsafe_allow_html=True,
        )

        rendered_response = st.write_stream(_stream_text(response))
        indicator.empty()

    add_assistant_message(rendered_response)


def _stream_text(text: str) -> Iterator[str]:
    for word in text.split(" "):
        yield f"{word} "
        time.sleep(STREAM_DELAY_SECONDS)


def _build_frontend_response(prompt: str) -> str:
    cleaned_prompt = " ".join(prompt.split())
    if not cleaned_prompt:
        return "I am ready when you are."

    return (
        "This is a frontend-only streaming preview. Your message was received "
        f"consistently as: \"{cleaned_prompt}\". When the backend API is connected, "
        "this same rendering path can display real streamed assistant chunks."
    )
