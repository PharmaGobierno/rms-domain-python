from fastapi import APIRouter

from .resources import tests

api_router = APIRouter(redirect_slashes=False)

api_router.include_router(
    tests.router,
    prefix="/tests",
    tags=["tests"],
)

__all__ = ["api_router"]
