from fastapi_jwt_auth import AuthJWT


def refresh_user_token_(authorize: AuthJWT):

    current_user = authorize.get_jwt_subject()
    new_access_token = authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}
