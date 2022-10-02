from .users import User
from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4
from typing import Optional
from datetime import datetime


class Tweet(BaseModel):
    tweet_id: UUID = Field(uuid4())
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