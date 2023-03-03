from aiohttp.web import Application

from app.web.logger import setup_logging
from app.web.routes import setup_routes

app = Application()


def setup_app():
    setup_logging()
    setup_routes(app)
    return app
