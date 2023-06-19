from fastapi import status, Depends
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT


async def refresh_(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_refresh_token_required()
        current_user = Authorize.get_jwt_subject()
        new_access_token = Authorize.create_access_token(subject=current_user)
        return {"access_token": new_access_token}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token, please provide a refresh token"
        )
