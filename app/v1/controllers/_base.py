from typing import Any, List, Optional, Type, TypeVar

from presentation.errors import ForbiddenError
from pydantic import BaseModel
from utils.logger import Logger

from app.v1.schemas.api_user_headers import ApiUserHeaders

BaseSchemaT = TypeVar("BaseSchemaT", bound=BaseModel)


class BaseController:
    def __init__(
        self,
        *,
        logger: Logger,
        api_user: Optional[ApiUserHeaders] = None,
        verbose: bool = True,
    ) -> None:
        self.logger = logger
        self.verbose = verbose
        self.api_user: ApiUserHeaders = api_user or ApiUserHeaders()

    def schema_validation(self, schema: Type[BaseSchemaT], *, data: Any) -> BaseSchemaT:
        if self.verbose:
            self.logger.log_info(f"[input] {data}")
        parsed_model: BaseSchemaT = schema.model_validate(data)
        return parsed_model

    def roles_validation(self, required_roles: List[str]):
        current_roles = set(self.api_user.roles)
        if self.verbose:
            self.logger.log_info(
                f"CURRENT_ROLES: {current_roles} | REQUIRED_ROLES: {required_roles}"
            )
        if not required_roles:
            return
        if not set(required_roles).intersection(current_roles):
            raise ForbiddenError(details="User does not have the required roles")
