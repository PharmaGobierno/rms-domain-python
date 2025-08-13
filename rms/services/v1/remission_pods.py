from typing import Iterator, List, Optional, Tuple

from rms.models.v1.remission_pods import RemissionPodsModel
from rms.repository_interfaces.v1.remission_pods import RemissionPodsRepositoryInterface

from ._base import BaseService


class RemissionsService(BaseService[RemissionPodsModel, RemissionPodsRepositoryInterface]):
    __model__ = RemissionPodsModel

    def get_by_tracking_id(
        self,
        tracking_id: str,
        *,
        tenant: Optional[List[str]] = None,
    ) -> Tuple[int, Iterator[RemissionPodsModel]]:
        count, result = self.repository.get_by_tracking_id(tracking_id, tenant=tenant)
        return count, map(lambda r: RemissionPodsModel(**r), result)

    def search_by_tracking(
        self,
        search_str: str,
        *,
        page: int,
        limit: int,
        created_at_gt: Optional[int] = None,
        created_at_lt: Optional[int] = None,
        tenants: Optional[List[str]] = None,
        events: Optional[List[str]] = None,
    ) -> Tuple[int, Iterator[RemissionPodsModel]]:
        count, result = self.repository.search_by_tracking(
            search_str,
            page=page,
            limit=limit,
            created_at_gt=created_at_gt,
            created_at_lt=created_at_lt,
            tenants=tenants,
            events=events,
        )
        return count, map(lambda r: RemissionPodsModel(**r), result)
