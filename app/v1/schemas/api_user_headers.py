import json
from base64 import b64decode
from typing import Any, List, Optional, Union

from presentation.errors import MissingParameterError
from pydantic import BaseModel, computed_field, model_validator


def auth_token_decode(
    b64_value: Union[str, bytes, memoryview], *, validate: bool = False
) -> bytes:
    if not isinstance(b64_value, str):
        if isinstance(b64_value, memoryview):
            b64_value = b64_value.tobytes()
        b64_value = b64_value.decode("utf-8")
    b64_value += "=" * ((4 - len(b64_value) % 4) % 4)
    return b64decode(b64_value, validate=validate)


class ApiUserHeaders(BaseModel):
    decoded_userinfo: dict = {}
    x_apigateway_api_userinfo: Optional[Union[str, bytes]] = None
    origin_timestamp: Optional[int] = None

    @model_validator(mode="before")
    @classmethod
    def decode_userinfo(cls, data: dict) -> Any:
        raw_userinfo: Union[str, bytes] = data.get("x_apigateway_api_userinfo", "")
        if raw_userinfo:
            try:
                decoded_bytes: bytes = auth_token_decode(raw_userinfo)
                data["decoded_userinfo"] = json.loads(decoded_bytes)
            except json.decoder.JSONDecodeError as e:
                raise ValueError(f"Invalid value on x-apigateway-api-userinfo {e}")
        return data

    @computed_field
    @property
    def tenant(self) -> List[str]:
        tenant: Optional[List[str]] = self.decoded_userinfo.get("tenant", [])
        if tenant is None:
            raise MissingParameterError(
                parameter="tenant",
                details="Can't find 'tenant' in decoded user data.",
                location=MissingParameterError.ERROR_LOCATION.HEADERS,
            )
        return tenant

    @computed_field
    @property
    def name(self) -> str:
        # getting name from keycloak (firstName + lastName)
        name: Optional[str] = self.decoded_userinfo.get("name")
        if name is None:
            raise MissingParameterError(
                parameter="name",
                details="Can't find 'name' in decoded user data.",
                location=MissingParameterError.ERROR_LOCATION.HEADERS,
            )
        return name

    @computed_field
    @property
    def email(self) -> str:
        email: Optional[str] = self.decoded_userinfo.get("email")
        if email is None:
            raise MissingParameterError(
                parameter="email",
                details="Can't find 'email' in decoded user data.",
                location=MissingParameterError.ERROR_LOCATION.HEADERS,
            )
        return email

    @computed_field
    @property
    def id(self) -> str:
        # getting id from keycloak bearer schema ('sub' is the unique identifier in keycloak)
        id: Optional[str] = self.decoded_userinfo.get("sub")
        if id is None:
            raise MissingParameterError(
                parameter="sub",
                details="Can't find 'id' in decoded user data.",
                location=MissingParameterError.ERROR_LOCATION.HEADERS,
            )
        return id

    @computed_field
    @property
    def roles(self) -> list[str]:
        # getting roles from keycloak bearer schema
        roles: Optional[list[str]] = self.decoded_userinfo.get("roles", [])
        if roles is None:
            raise MissingParameterError(
                parameter="roles",
                details="Can't find 'roles' in decoded user data.",
                location=MissingParameterError.ERROR_LOCATION.HEADERS,
            )
        return roles
