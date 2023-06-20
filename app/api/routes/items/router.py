from fastapi import APIRouter, status, Depends
from fastapi_jwt_auth import AuthJWT
from .services.create_item_ import create_item_
from .services.list_items_ import list_items_
from .services.get_item_ import get_item_
from .services.update_item_ import update_item_
from .services.delete_item_ import delete_item_
from .schemas import CreateItemRequestModel, CreateItemResponseModel, UpdateItemRequestModel, UpdateItemResponseModel
from app.api.utils_api.dependencies import get_db_session, login_required
from sqlalchemy.orm.session import Session
from app.api.utils_api.dependencies.pagenation_query_params import PaginationQueryParams

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
def list_items(
        jwt: AuthJWT = Depends(login_required),
        session: Session = Depends(get_db_session),
        page: PaginationQueryParams = Depends(PaginationQueryParams),
):
    response = list_items_(authorize=jwt, session=session, limit=page.limit, offset=page.offset,)
    return response


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CreateItemResponseModel)
def create_item(
        item: CreateItemRequestModel,
        authorize: AuthJWT = Depends(login_required),
        session: Session = Depends(get_db_session)
):
    response = create_item_(item=item, authorize=authorize, session=session)
    return response


@router.get("/{item_id}", status_code=status.HTTP_200_OK)
def get_item(
        item_id: int,
        authorize: AuthJWT = Depends(login_required),
        session=Depends(get_db_session)
):
    response = get_item_(item_id=item_id, authorize=authorize, session=session)
    return response


@router.put("/{item_id}", status_code=status.HTTP_200_OK, response_model=UpdateItemResponseModel)
def update_item(
        item_id: int,
        item: UpdateItemRequestModel,
        authorize: AuthJWT = Depends(login_required),
        session: Session = Depends(get_db_session)
):
    response = update_item_(item_id=item_id, item=item, authorize=authorize, session=session)
    return response


@router.delete("/{item_id}", status_code=status.HTTP_200_OK)
def delete_item(
        item_id: int,
        authorize: AuthJWT = Depends(login_required),
        session=Depends(get_db_session)
):
    response = delete_item_(item_id=item_id, authorize=authorize, session=session)
    return response
