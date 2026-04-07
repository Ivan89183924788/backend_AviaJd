from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.trip import TripCreate, TripPrice, TripUpdate, TripDelete
from app.services.trip_service import TripService
from database import get_db


router = APIRouter(prefix="/trip",tags=["Trips"])
@router.post("/")
async def create_trip(data:TripCreate,db:AsyncSession=Depends(get_db)):
    return await TripService.create_trip(db, data)

@router.post("/")
async def trip_price(data:TripPrice,db:AsyncSession=Depends(get_db)):
    return await TripService.trip_price(db, data)


@router.get("/")
async def get_trips(
        from_city:str|None=None,
        to_city:str|None=None,
        db:AsyncSession=Depends(get_db)):
    return await TripService.get_all(db,from_city,to_city)
@router.get("/{trip_id}")
async def get_trip(trip_id:int,db:AsyncSession=Depends(get_db)):
    trip=await TripService.get_by_id(db,trip_id)
    if not trip:
        raise HTTPException(status_code=404,detail="Trip not found")
    return trip

@router.put("/{trip_id}")
async def update_trip(trip_id:int,data:TripUpdate,db:AsyncSession=Depends(get_db)):
    trip_up=await TripService.update_trip(db,trip_id,data)
    if not trip_up:
        raise HTTPException(status_code=404, detail="Trip not found")
    return {
        "message": "Trip updated",
        "trip": trip_up
    }

@router.delete("/{trip_id}")
async def delete_trip(trip_id:int,data:TripDelete,db:AsyncSession=Depends(get_db)):
    trip_del=await TripService.delete_trip(db,trip_id,data)
    if not trip_del:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "message": "Trip deleted",
        "trip_del": trip_del
    }