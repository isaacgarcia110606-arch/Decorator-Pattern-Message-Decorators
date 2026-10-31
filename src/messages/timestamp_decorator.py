from .message_decorator import MessageDecorator


class TimestampDecorator(MessageDecorator):
    def __init__(self, wrapped, timestamp: str = "2026-10-30"):
        super().__init__(wrapped)
        self.timestamp = timestamp

    def render(self) -> str:
        return f"[{self.timestamp}] {self.wrapped.render()}"