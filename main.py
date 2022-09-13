# Python
from typing import List
import json

# Models
from models import User, UserBase, UserLogin, UserRegister, Tweet

# FastAPI
from fastapi import FastAPI, status, Body

app = FastAPI()


# Path operations

## Users

### Signup a new User

# The response is a User since it has everything but the password from the User
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user. ",
    tags=["Users"]
)

# UserRegister has everything including a password in order to signup. 
def signup(user: UserRegister = Body(...)):
    """
    Signs up a new User into the app

    Parameters:
    - Request body parameter
        - user: UserRegister

    Returns: JSON with the basic user information from the User model:
    - user_id: UUID
    - email: EmailStr
    - first_name: str
    - last_name: str
    - birth_date: date
    """
    with open ("users.json", "r+", encoding="utf-8") as f:
    
    # json.load converts the file into a json or dictionary. 
    # In this case, a list of dictionaries since there are multiple users and each user is a dictionary. 
        results = json.loads(f.read())
    
    # Create a dictionary based on the request body information. 
        user_dict = user.dict()

    # We are doing this since both UUID and date can't be converted into dictionaries naturally, it has to be manual with the str function.
    # From the key "user_id", change it into a str, same for "birth_date" so we have no issues with the json. 
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
    
    # This is necessary so we go to the start of the current list instead of creating a new one. 
        f.seek(0)
        f.write(json.dumps(results))
        return user

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
