from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import Booking
class BookingService:
    @staticmethod
    async def create_booking(db:AsyncSession,data):
        booking = Booking(**data.dict())
        db.add(booking)
        await db.commit()
        return booking

    @staticmethod
    async def booking_update(db: AsyncSession, data):
        booking_update = Booking(**data.dict())
        db.add(booking_update)
        await db.commit()
        return booking_update

    @staticmethod
    async def get_all(db:AsyncSession):
        bookings = await db.execute(select(Booking))
        return bookings.scalars().all()

    @staticmethod
    async def booking_get_one(db: AsyncSession, booking_id: int):
        result = await db.execute(select(Booking).where(Booking.id == booking_id))
        booking = result.scalar_one_or_none()
        if not booking:
            return None
        return booking

    @staticmethod
    async def booking_delete(db: AsyncSession, booking_id: int):
        result = await db.execute(select(Booking).where(Booking.id == booking_id))
        booking = result.scalar_one_or_none()
        if not booking:
            return None
        await db.delete(booking)
        await db.commit()
        return booking

