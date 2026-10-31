from datetime import date
from src.messages.plain_message import PlainMessage
from src.messages.urgent_decorator import UrgentDecorator
from src.messages.timestamp_decorator import TimestampDecorator


def test_individual_and_stacked_decorators():
    base_msg = PlainMessage("Server connection lost")
    today_str = str(date.today())

    assert base_msg.render() == "Server connection lost"

    urgent_msg = UrgentDecorator(base_msg)
    assert urgent_msg.render() == "URGENT: Server connection lost"

    timestamp_msg = TimestampDecorator(base_msg)
    assert timestamp_msg.render() == f"[{today_str}] Server connection lost"

    stacked_msg = TimestampDecorator(UrgentDecorator(base_msg))
    assert stacked_msg.render() == f"[{today_str}] URGENT: Server connection lost"