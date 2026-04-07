from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import Trip
class TripService:
    @staticmethod
    async def create_trip(db:AsyncSession,data):
        trip = Trip(**data.dict())
        db.add(trip)
        await db.commit()
        return trip

    @staticmethod
    async def trip_price(db: AsyncSession, price:float):
        trip_price = select(Trip).where(Trip.price == price)
        db.add(trip_price)
        await db.commit()
        return trip_price

    @staticmethod
    async def get_all(db:AsyncSession,
                      from_city:str|None=None,
                        to_city:str|None=None):
        result_f = select(Trip)
        if from_city:
            result_f = result_f.where(Trip.from_city == from_city)
        if to_city:
            result_f = result_f.where(Trip.to_city == to_city)
        results = await db.execute(result_f)
        return results.scalars().all()
    @staticmethod
    async def get_by_id(db:AsyncSession,trip_id:int):
        result=await db.execute(select(Trip).where(Trip.id == trip_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def update_trip(db: AsyncSession, trip_id: int, data):
        result = await db.execute(select(Trip).where(Trip.id == trip_id))
        trip = result.scalar_one_or_none()
        if not trip:
            return None
        if data.from_city is not None:
            trip.from_city = data.from_city
        if data.to_city is not None:
            trip.to_city = data.to_city
        if data.price is not None:
            trip.price= data.price
        await db.commit()
        await db.refresh(trip)
        return trip

    @staticmethod
    async def delete_trip(db: AsyncSession, trip_id: int):
        result = await db.execute(select(Trip).where(Trip.id == trip_id))
        trip_del = result.scalar_one_or_none()
        if not trip_del:
            return None
        await db.delete(trip_del)
        await db.commit()
        return trip_del