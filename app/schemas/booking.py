from pydantic import BaseModel

class BookingCreate(BaseModel):
    user_id:int
    trip_id:int

class BookingDelete(BaseModel):
    user_id:int
    trip_id:int

class BookingUpdate(BaseModel):
    status:str