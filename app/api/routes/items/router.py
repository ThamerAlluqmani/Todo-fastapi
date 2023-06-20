from fastapi import APIRouter, status, Depends
from fastapi_jwt_auth import AuthJWT
from .services.create_item import create_item
from .services.list_items import list_items
from .services.get_item import get_item
from .services.update_item import update_item
from .services.delete_item import delete_item
from .schemas import CreateRequestModel
from .schemas import UpdateRequestModel
from app.api.utils_api.dependencies import get_db_session


router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
async def list_items_(
        jwt: AuthJWT = Depends(),
        session=Depends(get_db_session)
):
    response = await list_items(authorize=jwt, session=session)
    return response


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_item_(
        item: CreateRequestModel,
        authorize: AuthJWT = Depends(),
        session=Depends(get_db_session)
):
    response = await create_item(item=item,authorize=authorize,session=session)
    return response


@router.get("/{item_id}", status_code=status.HTTP_200_OK)
async def get_item_(
        item_id: int,
        authorize: AuthJWT = Depends(),
        session=Depends(get_db_session)
):
    response = await get_item(item_id=item_id, authorize=authorize, session=session)
    return response


@router.put("/{item_id}", status_code=status.HTTP_200_OK)
async def update_item_(
        item_id: int,
        item: UpdateRequestModel,
        authorize: AuthJWT = Depends(),
        session=Depends(get_db_session)
):
    response = await update_item(item_id=item_id, item=item, authorize=authorize, session=session)
    return response


@router.delete("/{item_id}", status_code=status.HTTP_200_OK)
def delete_item_(
        item_id: int,
        authorize: AuthJWT = Depends(),
        session=Depends(get_db_session)
):
    response = delete_item(item_id=item_id, authorize=authorize, session=session)
    return response
