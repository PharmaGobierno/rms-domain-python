from os import getenv

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.libs import mongo_handler, pubsub_handler
from app.libs.logger_middleware import LoggerMiddleware
from app.v1.router import api_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(LoggerMiddleware)
    app.add_event_handler("startup", pubsub_handler.open_connection)
    app.add_event_handler("startup", mongo_handler.open_connection)
    app.add_event_handler("shutdown", mongo_handler.close_connection)
    # Routers
    app.include_router(api_router, prefix="/v1")
    return app


app = create_app()


@app.api_route("/", methods=["GET", "OPTIONS"])
async def health_check(request: Request):
    if request.method == "OPTIONS":
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "Authorization, Content-Type",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Max-Age": "600",
        }
        return JSONResponse(
            content=None, status_code=status.HTTP_204_NO_CONTENT, headers=headers
        )

    return f"{status.HTTP_200_OK}, OK"


if __name__ == "__main__":
    uvicorn.run(app, port=int(getenv("PORT", 8080)), host="0.0.0.0")
