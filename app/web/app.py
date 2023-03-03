from typing import Optional

from aiohttp.web import Application as AiohttpApplication

from app.web.config import Config, setup_config
from app.web.logger import setup_logging
from app.web.routes import setup_routes


class Application(AiohttpApplication):
    config: Optional[Config] = None


app = Application()


def setup_app() -> Application:
    setup_logging()
    setup_routes(app)
    # TODO: Вынести передачу путя до конфиг файла в другое место
    setup_config(app, "config.yaml")
    return app
