# Python
from typing import List

# Models
from models import User, UserBase, UserLogin

# FastAPI
from fastapi import FastAPI, status

from models.models import Tweet

app = FastAPI()


# Path operations

## Users

### Signup a new User
# The response is a User since it has everything but the password from 
# The User
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user. ",
    tags=["Users"]
)
def signup(

):
    pass

### Login a User
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user. ",
    tags=["Users"]
)
def login(

):
    pass

### Show all Users
@app.post(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users. ",
    tags=["Users"]
)
def show_users(

):
    pass

# Show a specific User
# We are obtaining info here
@app.get(
    path="/user/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a user. ",
    tags=["Users"]
)
def show_user(

):
    pass

### Delete a User
@app.delete(
    path="/user/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user. ",
    tags=["Users"]
)
def delete_user(

):
    pass

### Update a User
# Here we are updating the information
@app.put(
    path="/user/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user. ",
    tags=["Users"]
)
def update_user(
    
):
    pass

## Tweets

### Show all tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets. ",
    tags=["Tweets"]
)
def home():
    return {"Twitter API":"Working"}

### Create a new tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a new tweet. ",
    tags=["Tweets"]
)
def post_tweet(

):
    pass

### Show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet. ",
    tags=["Tweets"]
)
def show_tweet( 

):
    pass

### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet. ",
    tags=["Tweets"]
)
def delete_tweet( 

):
    pass

### Update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet. ",
    tags=["Tweets"]
)
def update_tweet( 

):
    pass
