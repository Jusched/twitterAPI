from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4
from typing import Any



class UserBase(BaseModel):
    user_id: UUID= Field(uuid4())
# UUID4 makes it so we don't have the same user_id
    email: EmailStr = Field(...)


class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=20
        )
    _message: str = Field(default="Login successful. ")

# User is used for other things without requiring the password
class User(UserBase):

    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )

class UserRegister(User):
        password: str = Field(
        ...,
        min_length=8,
        max_length=30
    )
