from dataclasses import dataclass


@dataclass(frozen=True)
class ChatMessage:
    role: str
    content: str
