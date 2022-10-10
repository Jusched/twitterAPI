from .users import User
from pydantic import BaseModel, Field, EmailStr


class Tweet(BaseModel):
    content: str = Field(
        ...,
        min_length=1,
        max_length=280
    )

    # It's a User class which has ID, email, first and last name but
    # No password since it is in the UserLogin class. 
    by: User = Field(...)