from app.store import setup_store
from .aiohttp_extansion import Application
from .config import setup_config
from .logger import setup_logging
from .routes import setup_routes


app = Application()


def setup_app() -> Application:
    setup_logging()
    setup_routes(app)
    # TODO: Вынести передачу путя до конфиг файла в другое место
    setup_config(app, "config.yaml")
    setup_store(app)
    return app
