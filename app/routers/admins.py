from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.schemas.admin_schemas import AdminCreate, AdminLogin
from app.services.admin_service import AdminService

from database import get_db

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/register")
async def register_admin(data:AdminCreate,db:AsyncSession=Depends(get_db)):
    return await AdminService.create_admin(db,data)
@router.post("/login")
async def login(data:AdminLogin,db:AsyncSession=Depends(get_db)):
    admin = await AdminService.login_admin(db,data.email,data.password)
    if not admin:
        raise HTTPException(status_code=401,detail="Incorrect email or password")
    return {"message":"login success","admin_id":admin.id}