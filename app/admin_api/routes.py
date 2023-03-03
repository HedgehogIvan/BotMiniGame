from aiohttp.web_app import Application

from app.admin_api.views import index


def setup_routes(app: Application):
    app.router.add_get('/index', index)
