from pydantic import BaseModel
from typing import Optional


class SignUp(BaseModel):
    username: str
    email: str | None = None
    password: str
    is_active: bool
    is_staff: bool

    class Config:
        from_attributes = True


class UserEdit(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    is_staff: Optional[bool] = None
    is_active: Optional[bool] = None