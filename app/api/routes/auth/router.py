from fastapi import APIRouter, status, Depends
from app.database import Session, engine
from .schemas import SignupModel, LoginModel
from fastapi_jwt_auth import AuthJWT
from .services.signup import signup
from .services.login import login
from .services.refresh_user_token import refresh_user_token
from .services.get_user_info import get_user_info
router = APIRouter()

session = Session(bind=engine)


@router.get("/")
async def get_user_info_(Authorize: AuthJWT = Depends()):
    response = await get_user_info(Authorize=Authorize)
    return response


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup_(user: SignupModel):
    response = await signup(user=user, session=session)
    return response


@router.post("/login", status_code=status.HTTP_200_OK)
async def login_(user: LoginModel, Authorize: AuthJWT = Depends()):
    response = await login(user=user, Authorize=Authorize)
    return response


# refresh token
@router.get("/refresh")
async def refresh_user_token(Authorize: AuthJWT = Depends()):
    response = await refresh_user_token(Authorize=Authorize)
    return response
