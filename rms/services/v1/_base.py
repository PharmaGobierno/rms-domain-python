from typing import Generic, Iterator, List, Optional, Tuple, Type, TypeVar, Union

from rms.models.v1._base import BaseModel
from rms.repository_interfaces.v1._base import BaseRepositoryInterface

RepositoryInterfaceT = TypeVar("RepositoryInterfaceT", bound="BaseRepositoryInterface")
ModelT = TypeVar("ModelT", bound="BaseModel")


class BaseService(Generic[ModelT, RepositoryInterfaceT]):
    __model__: Type[ModelT]

    def __init__(self, repository: RepositoryInterfaceT):
        self.repository = repository

    def create(self, entity: ModelT) -> None:
        data = entity.dict()
        self.repository.create(data)

    def update(self, entity_id, *, entity: ModelT) -> int:
        data = entity.dict()
        return self.repository.update(entity_id, data=data)

    def update_many(self, and_conditions: Optional[List[tuple]], *, data: dict) -> int:
        return self.repository.update_many(and_conditions, data=data)

    def set(
        self, entity_id, *, entity: ModelT, write_only_if_insert: bool = False
    ) -> int:
        data = entity.dict()
        return self.repository.set(
            entity_id, data=data, write_only_if_insert=write_only_if_insert
        )

    def get(
        self,
        entity_id,
        *,
        tenant: Optional[List[str]] = None,
        sort: Optional[List[Tuple[str, int]]] = None,
        projection: Optional[Union[list, dict]] = None,
    ) -> Optional[ModelT]:
        data: dict = self.repository.get(
            entity_id, tenant=tenant, sort=sort, projection=projection
        )
        if not data:
            return None
        return self.__model__(**data)

    def get_paginated(
        self,
        page: int,
        limit: int,
        *,
        tenant: Optional[List[str]] = None,
        and_conditions: Optional[List[tuple]] = None,
        sort: Optional[List[Tuple[str, int]]] = None,
        projection: Optional[List[str]] = None,
    ) -> Tuple[int, Iterator[ModelT]]:
        count, result = self.repository.get_paginated(
            page,
            limit,
            tenant=tenant,
            and_conditions=and_conditions,
            sort=sort,
            projection=projection,
        )
        return count, map(lambda itm: self.__model__(**itm), result)
