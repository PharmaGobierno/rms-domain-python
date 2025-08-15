from dataclasses import dataclass
from typing import Dict

from ._enums import EntityActionTypes
from .base_publisher import BaseKafkaMessage


@dataclass(kw_only=True)
class TmsOrderEventsKafkaMessage(BaseKafkaMessage):
    payload: dict
    event: str
    action_type: EntityActionTypes
    order_type: str = "REMISSION"
    origin_platform: str = "RMS"
    version: str = "1"

    def topic(self) -> str:
        """Returns the topic based in the order_type."""
        return "tms-order-events" + "-" + self.order_type

    def get_headers(self) -> Dict[str, str]:
        default_headers = super().get_headers()
        return {
            **default_headers,
            "event": self.event,
            "order_type": self.order_type,
            "action_type": self.action_type.value,
            "origin_platform": self.origin_platform,
        }
