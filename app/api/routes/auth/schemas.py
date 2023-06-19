from pydantic import BaseModel
from typing import Optional


class LoginModel(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "example@example.com",
                "password": "password",
            }
        }


class SignupModel(BaseModel):
    id: Optional[int]
    email: str
    password: str
    name: str
    phone: str
    university_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "example@example.com",
                "password": "password",
                "name": "John Doe",
                "phone": "0512345678",
                "university_id": 1,
            }
        }
