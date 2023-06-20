from pydantic import BaseModel


class CreateItemRequestModel(BaseModel):
    id: int | None
    title: str
    description: str | None
    owner_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "title": "example",
                "description": "example",
                "owner_id": 1
            }
        }


class CreateItemResponseModel(BaseModel):
    title: str
    description: str | None


class UpdateItemRequestModel(BaseModel):
    title: str | None
    description: str | None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "example",
                "description": "example",
            }
        }


class UpdateItemResponseModel(BaseModel):
    title: str
    description: str
