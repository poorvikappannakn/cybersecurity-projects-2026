from fastapi import Depends, HTTPException

from backend.services.security import get_current_user


def require_role(required_role: str):
    def role_checker(current_user: dict = Depends(get_current_user)):
        if current_user.get("role") != required_role:
            raise HTTPException(
                status_code=403,
                detail="Insufficient permissions"
            )

        return current_user

    return role_checker