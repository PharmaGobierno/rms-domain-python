from dataclasses import dataclass
from typing import List, Optional

from rms.models.submodels.v1.evidences import Evidence
from rms.models.v1.minified.users import UserMin

from ._base import EventfulModel, uuid_by_params
from ._enums import RemissionPodEvents


@dataclass(kw_only=True)
class RemissionPodEventsModel(EventfulModel[RemissionPodEvents]):
    __entity_name__ = "rms-remission-pod-events"

    tracking_id: str
    remission_pod_id: str
    author: UserMin
    load_id: Optional[str] = None
    metadata: Optional[dict] = None
    origin_platform: Optional[str] = None
    evidences: Optional[List[Evidence]] = None

    def __post_init__(self):
        super().__post_init__()
        self._id = uuid_by_params(self.tracking_id, self.event_timestamp)
