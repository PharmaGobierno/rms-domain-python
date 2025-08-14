from dataclasses import dataclass
from typing import Dict

from rms.models.v1.remission_pods import RemissionPodsModel

from ._enums import EntityActionTypes
from .base_publisher import BasePubsubMessage


@dataclass(kw_only=True)
class RemissionPodsPubsubMessage(BasePubsubMessage):
    payload: RemissionPodsModel
    origin_platform: str
    action_type: EntityActionTypes
    version: str = "1"

    @classmethod
    def topic(cls) -> str:
        return "rms-remission-pods"

    def get_attributes(self) -> Dict[str, str]:
        default_attributes = super().get_attributes()
        return {
            **default_attributes,
            "action_type": self.action_type.value,
            "origin_platform": self.origin_platform,
        }
