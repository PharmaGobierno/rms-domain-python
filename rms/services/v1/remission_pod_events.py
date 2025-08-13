from rms.models.v1.remission_pod_events import RemissionPodEventsModel
from rms.repository_interfaces.v1.remission_pod_events import (
    RemissionPodEventsRepositoryInterface,
)

from ._base import BaseService


class RemissionEventsService(
    BaseService[RemissionPodEventsModel, RemissionPodEventsRepositoryInterface]
):
    __model__ = RemissionPodEventsModel
