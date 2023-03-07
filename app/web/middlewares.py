import json

from aiohttp.web_exceptions import HTTPUnprocessableEntity, HTTPException
from aiohttp.web_middlewares import middleware
from aiohttp_apispec.middlewares import validation_middleware

from .aiohttp_extansion import Application, Request
from .utils import error_json_response

HTTP_ERROR_CODES = {
    400: "bad_request",
    401: "unauthorized",
    403: "forbidden",
    404: "not_found",
    405: "not_implemented",
    409: "conflict",
    500: "internal_server_error",
}


@middleware
async def error_handling_middleware(request: Request, handler):
    try:
        response = await handler(request)
        return response
    except HTTPUnprocessableEntity as e:
        return error_json_response(
            http_status=400,
            status="bad_request",
            message=e.reason,
            data=json.loads(e.text),
        )
    # TODO: Переделать реакцию 409 ошибки
    except HTTPException as e:
        return error_json_response(
            http_status=e.status,
            status=HTTP_ERROR_CODES[e.status],
            message=str(e),
        )
    except Exception as e:
        request.app.logger.error("Exception", exc_info=e)
        return error_json_response(
            http_status=500, status="internal server error", message=str(e)
        )


def setup_middlewares(app: Application):
    app.middlewares.append(error_handling_middleware)
    app.middlewares.append(validation_middleware)
