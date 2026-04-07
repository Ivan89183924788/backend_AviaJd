from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.models import Admin


class AdminService:
    @staticmethod
    async def create_admin(db:AsyncSession,data):
        admin=Admin(**data.dict())
        db.add(admin)
        await db.commit()
        await db.refresh(admin)
        return admin
    @staticmethod
    async def login_admin(db:AsyncSession,email_ad:str,password_ad:str):
        result=await db.execute(select(Admin).where(Admin.email_ad==email_ad))
        admin=result.scalar_one_or_none()
        if not admin or admin.password_ad != password_ad:
            return None
        return admin