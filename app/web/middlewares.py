from app.web.aiohttp_extansion import Application

from aiohttp_apispec.middlewares import validation_middleware


def setup_middlewares(app: Application):
    app.middlewares.append(validation_middleware)
