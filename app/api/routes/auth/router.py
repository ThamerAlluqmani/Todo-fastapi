from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from .schemas import SignupRequestModel, LoginResponseModel, SignupResponseModel
from fastapi_jwt_auth import AuthJWT  # type: ignore
from .services.signup_ import signup_
from .services.login_ import login_
from .services.refresh_user_token_ import refresh_user_token_
from .services.get_user_info_ import get_user_info_
from .services.delete_user_ import delete_user_
from app.api.utils_api.dependencies import (
    get_db_session,
    login_required,
    refresh_token_required,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/")
def get_user_info(
    authorize: AuthJWT = Depends(login_required),
    session: Session = Depends(get_db_session),
):
    response = get_user_info_(authorize=authorize, session=session)
    return response


@router.post(
    "/signup", status_code=status.HTTP_201_CREATED, response_model=SignupResponseModel
)
def signup(user: SignupRequestModel, session: Session = Depends(get_db_session)):
    response = signup_(user=user, session=session)
    return response


@router.post("/login", status_code=status.HTTP_200_OK)
def login(
    user: LoginResponseModel,
    authorize: AuthJWT = Depends(),
    session: Session = Depends(get_db_session),
):
    response = login_(user=user, authorize=authorize, session=session)
    return response


# refresh token
@router.post("/refresh")
def refresh_user_token(authorize: AuthJWT = Depends(refresh_token_required)):
    response = refresh_user_token_(authorize=authorize)
    return response


@router.delete("/delete_user")
def delete_user(
    authorize: AuthJWT = Depends(), session: Session = Depends(get_db_session)
):
    response = delete_user_(authorize=authorize, session=session)
    return response
