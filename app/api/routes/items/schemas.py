from pydantic import BaseModel


class CreateRequestModel(BaseModel):
    title: str
    description: str = None
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


class CreateResponseModel(BaseModel):
    title: str
    description: str = None


class UpdateResponseModel(BaseModel):
    id: int
    name: str
    description: str = None


class UpdateRequestModel(BaseModel):
    name: str
    description: str = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "example",
                "description": "example",
            }
        }

# class GetResponseModel(BaseModel):
#     id: int
#     name: str
#     description: str = None
#
#
# class DeleteRequestModel(BaseModel):
#     id: int
#     name: str
#     description: str = None
