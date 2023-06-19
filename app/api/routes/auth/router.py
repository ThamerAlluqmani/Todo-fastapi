from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from app.database import Session, engine
from .schemas import SignupModel, LoginModel
from fastapi_jwt_auth import AuthJWT
from .services.create_user import signup_
from .services.login_user import login_
from .services.refresh_user_token import refresh_

router = APIRouter()

session = Session(bind=engine)


@router.get("/")
async def root(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
        current_user = Authorize.get_jwt_subject()
        return {"message": f"Hello {current_user}"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: SignupModel):
    response = await signup_(user=user, session=session)
    return response


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(user: LoginModel, Authorize: AuthJWT = Depends()):
    response = await login_(user=user, Authorize=Authorize)
    return response


# refresh token
@router.get("/refresh")
async def refresh(Authorize: AuthJWT = Depends()):
    response = await refresh_(Authorize=Authorize)
    return response
