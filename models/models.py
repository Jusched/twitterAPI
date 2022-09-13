# Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional

# Pydantic 
from pydantic import BaseModel, EmailStr, Field

# FastAPI
from fastapi import FastAPI


# Everything inherits from UserBase because it has the minimum requirements
# To initialize an user. 
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=30
    )

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
    birth_date: Optional[date] = Field(default=None)

class UserRegister(User):
        password: str = Field(
        ...,
        min_length=8,
        max_length=30
    )


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=280
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    # It's a User class which has ID, email, first and last name but
    # No password since it is in the UserLogin class. 
    by: User = Field(...)