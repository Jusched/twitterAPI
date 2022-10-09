# Python
from typing import List
from uuid import UUID, uuid4

# Models
from models import User, UserRegister, UserLogin

# FastAPI, JSON, Pydantic and Bcrypt
from fastapi import APIRouter, Body, Path, status, HTTPException
import json
import bcrypt


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


## Users
### Signup a new User

# The response is a User since it has everything but the password from the User
@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user. "
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
    """

    with open("db/users.json", "r+", encoding="utf-8") as f:
        results = json.load(f)
        user_dict = user.dict()

# Checking if any email is repeated
        if any(users['email'] == user.email for users in results):
            raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exist!")
        
# Process to encrypt the password
        user.password = user.password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashpass = bcrypt.hashpw(user.password,salt)
        user_dict["password"] = hashpass
        results.append(user_dict)
        f.seek(0)
        json.dump(results, f, default=str, indent=4)
        return user


### Login a User
@router.post(
    path="/login",
    response_model=UserLogin,
    status_code=status.HTTP_200_OK,
    summary="Login a user. "
)
def login(user: UserLogin):
    """
    Logins a user into the app verificating the credentials.

    Parameters: 
    Request body parameter.
        - email: EmailStr
        - password: str

    Returns: JSON from the User class with the information of the logged user. 
    """
    with open("db/users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())

# A variable will have each value of the list of dictionaries for the users and check if both email and password are correct.
        for address in range(len(results)):
            cont = results[address]

# If both email and password are correct for the same user in the database, login successful. 
            if cont["email"] == user.email and cont["password"] == user.password:
                return user
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Your email or password is incorrect."
            )



### Show all Users
@router.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users. "
)
def show_all(

):
    """
    Show all users registered in the app. 

    Parameters: None

    Returns JSON list with all the users in the app, along with the following keys:
    - user_id: UUID
    - email: EmailStr
    - first_name: str
    - last_name: str
    """
    with open("db/users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results


# Show a specific User
# We are obtaining info here
@router.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a user. "
)
def show_user(user_id = UUID == Path(
    ...,
    title="User_ID",
    description="This is the person ID."
)):
    """
    Shows a specific user in the database. 

    Parameters: 
    Path parameters.
        - user_id: UUID

    Returns: 
    User JSON with the data from the selected user. 
    - user: User
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
    """
    with open("db/users.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        id = str(user_id)
    for user in results:
        if user["user_id"] == id:
            return user

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This user ID does not belong to any existing user."
        )

### Delete a User
@router.delete(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user. ")

def delete_user(user_id = UUID == Path(
    ...,
    title="User ID",
    example=(uuid4())
    )
):

    """
    Delete a user based on its user_id.

    Parameters: 
    Path parameters.
        - user_id: UUID

    Returns:
    User JSON with the deleted data. 
    - user: User class
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
    """

    with open("db/users.json", "r+", encoding="utf-8") as f:
        results = json.load(f)
        user_id = str(user_id)

        for id in range(len(results)):
            user = results[id]
            if user_id == user["user_id"]:
                results.pop(id)
                f.truncate(0)
                f.seek(0)
                json.dump(results, f, default=str, indent=4)
                return user
        else:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail="This user ID does not exist."
            )

### Update a User
# Here we are updating the information
@router.put(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user. "
)
def update_tweet(user_id: UUID = Path(
            ...,
            title="User ID",
            description="This is the user ID",
            example="3fa85f64-5717-4562-b3fc-2c963f66afa3"
        ),
        userEd: User = Body(
            ...,
            title="Data to update. ",
            description="Enter the data you need to update. "
            )
    ):
    """
    Update a user based on its user_id

    Parameters: 
    Path parameters.
        - user_id: UUID
    Body parameters.
        - user: User
            - email: EmailStr
            - first_name: str
            - last_name: str

    Returns:
    User JSON with the updated data. 
    - email: EmailStr
    - first_name: str
    - last_name: str
    """
    with open("db/users.json", "r+", encoding="utf-8") as f: 
        results = json.load(f)
        for user in results:
            if str(user_id) == user["user_id"]:
                user["email"] = userEd.email
                user["first_name"] = userEd.first_name
                user["last_name"] = userEd.last_name
                f.truncate(0)
                f.seek(0)
                json.dump(results, f, default=str, indent=4)
                return user

        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="This user ID does not exist. "
            )
