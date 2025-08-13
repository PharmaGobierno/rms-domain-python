from dataclasses import dataclass
from typing import Optional

from rms.models.v1.minified.users import UserMin

from ._base import UpdatableModel, uuid_by_params
from ._enums import RemissionEvents


@dataclass(kw_only=True)
class RemissionPodsModel(UpdatableModel):
    __entity_name__ = "rms-remission-pods"

    tracking_id: str
    order_id: str
    current_event: Optional[RemissionEvents] = None
    current_event_timestamp: Optional[int] = None
    last_load: Optional[str] = None
    last_ans: Optional[UserMin] = None
    last_validator: Optional[UserMin] = None
    order_supply: Optional[str] = None
    remission_pod_evaluation_id: Optional[str] = None

    def __post_init__(self):
        super().__post_init__()
        self._id = uuid_by_params(self.tracking_id)
