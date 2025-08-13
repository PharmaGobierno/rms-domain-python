from dataclasses import dataclass
from typing import Dict

from rms.models.v1.remission_pods import RemissionPodsModel

from ._enums import EntityActionTypes
from .base_publisher import BasePubsubMessage


@dataclass(kw_only=True)
class RemissionPodsPubsubMessage(BasePubsubMessage):
    payload: RemissionPodsModel
    event: str
    action_type: EntityActionTypes
    version: str = "1"

    @classmethod
    def topic(cls) -> str:
        return "rms-remission-pods"

    def get_attributes(self) -> Dict[str, str]:
        default_attributes = super().get_attributes()
        return {
            **default_attributes,
            "event": self.event,
            "action_type": self.action_type.value,
        }
