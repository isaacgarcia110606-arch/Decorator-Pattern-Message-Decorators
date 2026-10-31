from datetime import date
from src.messages.message_decorator import MessageDecorator


class TimestampDecorator(MessageDecorator):
    def __init__(self, wrapped: MessageDecorator, timestamp: str = None):
        super().__init__(wrapped)
        # Si no envían fecha, usa la fecha de hoy en formato YYYY-MM-DD
        self.timestamp = timestamp if timestamp else str(date.today())

    def render(self) -> str:
        return f"[{self.timestamp}] {self.wrapped.render()}"