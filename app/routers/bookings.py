from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.booking import BookingCreate, BookingDelete, BookingUpdate
from app.schemas.trip import TripPrice
from app.services.booking_service import BookingService
from app.services.trip_service import TripService
from database import get_db

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.get("/")
async def get_booking(db:AsyncSession=Depends(get_db)):
    return await BookingService.get_all(db)



@router.post("/")
async def booking_price(data:TripPrice,db:AsyncSession=Depends(get_db)):
    return await TripService.trip_price(db, data)

@router.post("/")
async def booking_update(data:BookingUpdate,db:AsyncSession=Depends(get_db)):
    return await BookingService.booking_update(db, data)

@router.get("/")
async def get_booking_one(db:AsyncSession=Depends(get_db)):
    return await BookingService.booking_get_one(db)


@router.delete("/me/{booking_id}")
async def delete_me_booking(booking_id:int,data:BookingDelete,db:AsyncSession=Depends(get_db)):
    booking=await BookingService.booking_delete(db, booking_id,data)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {
        "message": "Booking deleted",
        "booking": booking
    }