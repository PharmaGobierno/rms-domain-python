"""
* :description: Namespace API
"""

from typing import Annotated

from fastapi import APIRouter, Depends, Header, Request, Response, status

from app.libs import mongo_handler, pubsub_handler
from app.v1.controllers._base import BaseController
from app.v1.exceptions.handler import exception_handler
from app.v1.schemas.api_user_headers import ApiUserHeaders

router = APIRouter()


# ? [GET] <— /v1/tests/headers
@router.get("/headers")
@exception_handler(response_status=status.HTTP_200_OK)
async def get_headers(
    request: Request,
    response: Response,
    api_user_headers: Annotated[ApiUserHeaders, Header()],
    db_manager=Depends(mongo_handler.get_manager),
    pubsub_manager=Depends(pubsub_handler.get_manager),
) -> dict:
    ctrl = BaseController(logger=request.state.logger, api_user=api_user_headers)
    ctrl.logger.log_info(request.headers.items())
    ctrl.roles_validation(
        ["Jefe_de_farmacia", "Admin"]
    )  # throws exception if any of this roles are not in decoded token
    return {
        "tenant": ctrl.api_user.tenant,  # throws exception only when accessed and data is None
        "api_user": ctrl.api_user.model_dump(),
        "origin_timestamp": api_user_headers.origin_timestamp,
    }
