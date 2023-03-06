from typing import Optional

from sqlalchemy import select, ChunkedIteratorResult, insert

from ...admin.models import Admin, AdminModel
from ...base.base_accessor import BaseAccessor


class AdminAccessor(BaseAccessor):
    async def create_admin(self, login: str, password: str) -> Admin:
        query = insert(AdminModel).values(login=login, password=password)

        async with self.app.database.session() as session:
            res = await session.execute(query)
            # Достаем планируемый id для админа в базе
            id_ = res.inserted_primary_key[0]

            await session.commit()

            return Admin(id_, login, password)

    async def get_by_login(self, login: str) -> Admin | None:
        admin: Optional[AdminModel] = None
        query = select(AdminModel).where(AdminModel.login == login)

        async with self.app.database.session() as session:
            res: ChunkedIteratorResult = await session.execute(query)

            try:
                admin: AdminModel = res.scalars().first()
            except:
                print("Не получилось достать админа")

            if admin:
                return Admin(admin.id, admin.login, admin.password)
            else:
                return None
