from pydantic import BaseModel
class AdminCreate(BaseModel):
    email_ad: str
    password_ad: str
    full_name_ad: str|None=None
    phone_ad:str|None=None

class AdminLogin(BaseModel):
    email_ad: str
    password_ad: str
