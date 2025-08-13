from abc import abstractmethod
from typing import Iterator, List, Optional, Tuple, Union

from ._base import BaseRepositoryInterface


class RemissionPodsRepositoryInterface(BaseRepositoryInterface):
    @abstractmethod
    def get_by_tracking_id(
        self,
        tracking_id: str,
        *,
        tenant: Optional[List[str]] = None,
        sort: Optional[List[Tuple[str, int]]] = None,
        projection: Optional[Union[list, dict]] = None,
        limit: Optional[int] = None,
    ) -> Tuple[int, Iterator[dict]]:
        raise NotImplementedError

    @abstractmethod
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
    ) -> Tuple[int, List[dict]]:
        raise NotImplementedError
