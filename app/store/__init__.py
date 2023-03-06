import typing

from .database.database import Database

if typing.TYPE_CHECKING:
    from ..web.aiohttp_extansion import Application


class Store:
    def __init__(self, app: "Application"):
        from .admin.accessor import AdminAccessor

        self.admins = AdminAccessor(app)


def setup_store(app: "Application"):
    app.database = Database(app)
    app.on_startup.append(app.database.connect)
    app.on_cleanup.append(app.database.disconnect)
    app.store = Store(app)
