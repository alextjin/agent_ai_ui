import streamlit as st


def configure_page() -> None:
    st.set_page_config(
        page_title="AI Chat",
        page_icon="AI",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def apply_global_styles() -> None:
    st.markdown(
        """
        <style>
            :root {
                --app-bg: #f8fafc;
                --panel-bg: #ffffff;
                --text-primary: #111827;
                --text-muted: #6b7280;
                --border-soft: #e5e7eb;
                --accent: #2563eb;
                --assistant-bg: #ffffff;
                --user-bg: #eef2ff;
            }

            .stApp {
                background: var(--app-bg);
                color: var(--text-primary);
            }

            [data-testid="stSidebar"] {
                background: #ffffff;
                border-right: 1px solid var(--border-soft);
            }

            [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
                color: var(--text-muted);
            }

            .block-container {
                max-width: 960px;
                padding: 2rem 1.5rem 7.5rem;
            }

            .chat-hero {
                margin: 0 auto 1.5rem;
                max-width: 760px;
                text-align: center;
            }

            .chat-hero h1 {
                margin: 0 0 0.45rem;
                color: var(--text-primary);
                font-size: 2rem;
                font-weight: 650;
                letter-spacing: 0;
            }

            .chat-hero p {
                margin: 0;
                color: var(--text-muted);
                font-size: 0.98rem;
            }

            .chat-shell {
                max-width: 760px;
                margin: 0 auto;
            }

            .message-meta {
                margin: 0.35rem 0 0.15rem;
                color: var(--text-muted);
                font-size: 0.78rem;
                font-weight: 600;
            }

            .stChatMessage {
                max-width: 760px;
                margin-left: auto;
                margin-right: auto;
                padding: 0.65rem 0;
            }

            [data-testid="stChatMessageContent"] {
                border: 1px solid var(--border-soft);
                border-radius: 8px;
                padding: 0.8rem 0.95rem;
                box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
            }

            [data-testid="stChatMessageContent"] p {
                line-height: 1.65;
            }

            [data-testid="stChatInput"] {
                max-width: 760px;
                margin: 0 auto;
            }

            [data-testid="stChatInput"] textarea {
                border-radius: 8px;
            }

            .sidebar-title {
                margin: 0 0 0.35rem;
                font-size: 1.1rem;
                font-weight: 650;
            }

            .sidebar-section {
                margin-top: 1.2rem;
                padding-top: 1rem;
                border-top: 1px solid var(--border-soft);
            }

            .sidebar-placeholder {
                padding: 0.7rem 0;
                color: var(--text-muted);
                font-size: 0.9rem;
            }

            .typing-indicator {
                color: var(--text-muted);
                font-size: 0.9rem;
                line-height: 1.6;
            }

            .typing-indicator::after {
                content: "";
                display: inline-block;
                width: 1.2rem;
                text-align: left;
                animation: typing-dots 1.2s steps(4, end) infinite;
            }

            @keyframes typing-dots {
                0% { content: ""; }
                25% { content: "."; }
                50% { content: ".."; }
                75%, 100% { content: "..."; }
            }

            @media (max-width: 720px) {
                .block-container {
                    padding: 1.25rem 1rem 7rem;
                }

                .chat-hero {
                    text-align: left;
                }

                .chat-hero h1 {
                    font-size: 1.55rem;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header() -> None:
    st.markdown(
        """
        <div class="chat-hero">
            <h1>AI Assistant</h1>
            <p>A clean workspace for focused conversations.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
