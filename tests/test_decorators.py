from message import PlainMessage
from urgent_decorator import UrgentDecorator
from timestamp_decorator import TimestampDecorator


def test_individual_and_stacked_decorators():
    base_msg = PlainMessage("Server connection lost")
    timestamp = "2026-10-30 14:00"

    # 1. Plain message
    assert base_msg.render() == "Server connection lost"

    # 2. Urgent Decorator
    urgent_msg = UrgentDecorator(base_msg)
    assert urgent_msg.render() == "URGENT: Server connection lost"

    # 3. Stacked: Timestamp(Urgent(Plain))
    stacked_msg = TimestampDecorator(
        UrgentDecorator(base_msg), 
        timestamp=timestamp
    )
    assert stacked_msg.render() == f"[{timestamp}] URGENT: Server connection lost"

    # 4. Order verification: Urgent(Timestamp(Plain))
    reverse_stacked_msg = UrgentDecorator(
        TimestampDecorator(base_msg, timestamp=timestamp)
    )
    assert reverse_stacked_msg.render() == f"URGENT: [{timestamp}] Server connection lost"