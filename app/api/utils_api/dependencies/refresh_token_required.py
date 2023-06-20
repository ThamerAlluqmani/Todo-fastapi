from fastapi import Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT


def refresh_token_required(authorize: AuthJWT = Depends()):
    try:
        authorize.jwt_refresh_token_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token, please provide a refresh token"
        )
    return authorize
