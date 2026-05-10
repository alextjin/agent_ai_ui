import streamlit as st

from src.utils.session_state import reset_chat_session


def render_sidebar() -> None:
    with st.sidebar:
        st.markdown('<div class="sidebar-title">AI Chat</div>', unsafe_allow_html=True)
        st.caption("Frontend workspace")

        if st.button("New chat", use_container_width=True):
            reset_chat_session()
            st.rerun()

        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.subheader("Conversations")
        st.markdown(
            '<div class="sidebar-placeholder">Recent chats will appear here.</div>',
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.subheader("Settings")
        st.selectbox("Model", ["Backend default"], disabled=True)
        st.toggle("Streaming", value=True, disabled=True)
        st.markdown("</div>", unsafe_allow_html=True)
