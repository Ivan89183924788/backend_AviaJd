from pydantic import BaseModel

class TripCreate(BaseModel):
    from_city:str | None=None
    to_city:str | None=None
    price:float

class TripPrice(BaseModel):
    price:float

class TripUpdate(BaseModel):
    from_city:str | None=None
    to_city:str | None=None
    price:float

class TripDelete(BaseModel):
    from_city:str | None=None
    to_city:str | None=None
    price:float