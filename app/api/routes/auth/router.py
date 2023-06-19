from fastapi import APIRouter, status, Depends
from .schemas import SignupRequestModel, LoginResponseModel
from fastapi_jwt_auth import AuthJWT
from .services.signup import signup
from .services.login import login
from .services.refresh_user_token import refresh_user_token
from .services.get_user_info import get_user_info

router = APIRouter()


@router.get("/")
async def get_user_info_(authorize: AuthJWT = Depends()):
    response = await get_user_info(authorize=authorize)
    return response


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup_(user: SignupRequestModel):
    response = await signup(user=user)
    return response


@router.post("/login", status_code=status.HTTP_200_OK)
async def login_(user: LoginResponseModel, authorize: AuthJWT = Depends()):
    response = await login(user=user, authorize=authorize)
    return response


# refresh token
@router.get("/refresh")
async def refresh_user_token_(authorize: AuthJWT = Depends()):
    response = await refresh_user_token(authorize=authorize)
    return response
