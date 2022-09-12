# Python
from typing import List

# Models
from models import User, UserBase, UserLogin

# FastAPI
from fastapi import FastAPI, status

app = FastAPI()

@app.get(path="/")
def home():
    return {"Twitter API":"Working"}

# Path operations

## Users

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