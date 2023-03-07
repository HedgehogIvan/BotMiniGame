from hashlib import sha256
from typing import Optional

from aiohttp.web_exceptions import HTTPForbidden, HTTPConflict
from aiohttp.web_response import json_response
from aiohttp_apispec import request_schema, response_schema
from aiohttp_session import new_session

from ..web.aiohttp_extansion import View
from .models import Admin
from .shemes import AdminScheme


class CreateAdminView(View):
    @request_schema(AdminScheme)
    @response_schema(AdminScheme)
    async def post(self):
        # TODO: Добавить проверку, что это нужный админ
        # Временное получение даты, до схем
        data = await self.request.json()

        login = data["login"]
        password = await self._hash_password()

        admin: Admin = await self.store.admins.get_by_login(login)

        if not admin:
            new_admin = await self.store.admins.create_admin(login, password)
            return json_response(data={
                "id": new_admin.id,
                "login": login
            })
        else:
            raise HTTPConflict

    async def _hash_password(self):
        """
        Хэширует пароль, полученный при запросе
        :return: Хэшированный пароль или None
        """
        data: dict = await self.request.json()

        if "password" in data:
            return sha256(data["password"].encode("utf-8")).hexdigest()
        return None
