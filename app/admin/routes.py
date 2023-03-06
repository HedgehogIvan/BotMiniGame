from ..web.aiohttp_extansion import Application

from .views import CreateAdminView


def setup_routes(app: Application):
    app.router.add_view("/create.admin", CreateAdminView)
