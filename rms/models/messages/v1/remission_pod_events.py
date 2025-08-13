from dataclasses import dataclass
from typing import Dict

from rms.models.v1.remission_pod_events import RemissionPodEventsModel

from ._enums import EntityActionTypes
from .base_publisher import BasePubsubMessage


@dataclass(kw_only=True)
class RemissionPodEventsPubsubMessage(BasePubsubMessage):
    payload: RemissionPodEventsModel
    event: str
    action_type: EntityActionTypes
    origin_platform: str
    version: str = "1"

    @classmethod
    def topic(cls) -> str:
        return "rms-remission-pod-events"

    def get_attributes(self) -> Dict[str, str]:
        default_attributes = super().get_attributes()
        return {
            **default_attributes,
            "event": self.event,
            "action_type": self.action_type.value,
            "origin_platform": self.origin_platform,
        }
