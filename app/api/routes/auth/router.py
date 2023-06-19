from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from app.database import Session, engine
from .schemas import SignupModel, LoginModel
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder


auth_router = APIRouter()

session = Session(bind=engine)


@auth_router.get("/")
async def root(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
        current_user = Authorize.get_jwt_subject()
        return {"message": f"Hello {current_user}"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


@auth_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: SignupModel):
    db_email = session.query(User).filter(User.email == user.email).first()
    if db_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    new_user = User(
        email=user.email,
        password=generate_password_hash(user.password),
        name=user.name,
        phone=user.phone,
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def login(user: LoginModel, Authorize: AuthJWT = Depends()):
    db_user = session.query(User).filter(User.email == user.email).first()
    if db_user and check_password_hash(db_user.password, user.password):
        access_token = Authorize.create_access_token(subject=db_user.email)
        refresh_token = Authorize.create_refresh_token(subject=db_user.email)
        response = {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
        return jsonable_encoder(response)
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")


# refresh token
@auth_router.get("/refresh")
async def refresh(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_refresh_token_required()
        current_user = Authorize.get_jwt_subject()
        new_access_token = Authorize.create_access_token(subject=current_user)
        return {"access_token": new_access_token}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid token, please provide a refresh token")