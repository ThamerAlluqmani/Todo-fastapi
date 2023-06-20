from fastapi import Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT


def login_required(authorize: AuthJWT = Depends()):
    try:
        authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return authorize.get_jwt_subject()
