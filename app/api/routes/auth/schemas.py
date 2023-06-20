from pydantic import BaseModel


class LoginResponseModel(BaseModel):
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


class SignupRequestModel(BaseModel):
    id: int | None
    email: str
    password: str
    name: str
    phone: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "example@example.com",
                "password": "password",
                "name": "John Doe",
                "phone": "0512345678",
            }
        }


class SignupResponseModel(BaseModel):
    email: str
    name: str
    phone: str
