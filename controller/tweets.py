# Python
from typing import List
from uuid import UUID

# Models
from models.tweets import Tweet

# FastAPI and JSON
from fastapi import APIRouter, status, Body, Path, Form, HTTPException
import json

router = APIRouter(
    prefix="/tweets",
    tags=["Tweets"]
)

## Tweets
### Show all tweets
@router.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets. "
)
def home():
    """
    Show all tweets registered in the app. 

    Parameters: None

    Returns JSON list with all the tweets in the app, along with the following keys:
    - tweet_id: UUID
    - content: str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User
    """
    with open("db/tweets.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results 

### Create a new tweet
@router.post(
    path="/tweets/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a new tweet. "
)
def post_tweet(tweet: Tweet = Body(...)):
    """
    Posts a tweet in the app

    Parameters:
    - Request body parameters:
        - tweet: Tweet
            - content: str
            - created_at: datetime
            - updated_at: Optional[datetime]

    Returns: JSON with the tweet
    - tweet_id: UUID
    - content: str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User  
    """
    with open("db/tweets.json", "r+", encoding="utf-8") as f:
        results = json.load(f)
        tweet_dict = tweet.dict()
        results.append(tweet_dict)
        f.seek(0)
        json.dump(results, f, default=str, indent=4)
        return tweet

### Show a tweet
@router.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a specific tweet"
)

def show_tweet(tweet_id = UUID == Path(
    ...,
    title="Tweet ID",
    description="This is the tweet ID."
)):
    """
    Shows a specific tweet in the database. 

    Parameters: 
    Path parameter.
        - tweet_id: UUID

    Returns: 
    Tweet JSON with the data from the selected tweet. 
    - tweet: Tweet
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
            - user_id: UUID
            - email: EmailStr
            - first_name: str
            - last_name: str
    """
    with open("db/tweets.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        id = str(tweet_id)
    for tweet in results:
        if tweet["tweet_id"] == id:
            return tweet

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This tweet ID does not belong to any existing tweet."
        )

### Delete a tweet
@router.delete(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet. "
)
def delete_tweet(tweet_id = UUID == Path(
        ...,
        title="Tweet ID",
        example="3fa85f64-5717-4562-b3fc-2c963f66afa8"
)
):
    """
    Delete a tweet based on its tweet_id.

    Parameters: 
    Path parameter.
        - tweet_id: UUID

    Returns:    
    User JSON with the deleted data. 
    - tweet: Tweet
        - tweet_id: UUID
        - content: str
        - by: User
            - user_id: UUID
            - email: EmailStr
            - first_name: str
            - last_name: str
    """
    with open("db/tweets.json", "r+", encoding="utf-8") as f:
        results = json.load(f)
        tweet_id = str(tweet_id)

        for id in range(len(results)):
            tweet = results[id]
            if tweet_id == tweet["tweet_id"]:
                results.pop(id)
                f.truncate(0)
                f.seek(0)
                json.dump(results, f, default=str, indent=4)
                return tweet
        else:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail="This tweet ID does not exist."
            )

### Update a tweet
@router.put(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet. "
)
def update_tweet(tweet_id = UUID == Path(
    ...,
    title="Tweet ID",
    description="This is the tweet ID. ",
    example="3fa85f64-5717-4562-b3fc-2c963f66afa8"
    ),
    content= str == Form(
        ...,
       min_length=1,
       max_length=280,
       title="Tweet content. ",
       description="This is the content of the tweet."
    )
):
    """
    Update a tweet based on its tweet_id

    Parameters: 
    Path parameter.
        - tweet_id: UUID
    Body parameter.
        - content = str

    Returns:
    Tweet JSON with the updated data. 
    - tweet: Tweet
    - tweet_id: UUID
    - content: str
    - by: User
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
    """
    with open("db/tweets.json", "r+", encoding="utf-8") as f: 
        results = json.load(f)
        for tweet in results:
            if tweet_id == tweet["tweet_id"]:
                tweet['content'] = content
                f.truncate(0)
                f.seek(0)
                json.dump(results, f, default=str, indent=4)
                return tweet
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="This tweet ID does not exist. "
            )
