# Python
from typing import List

# Models
from models.tweets import Tweet

# FastAPI and JSON
from fastapi import APIRouter, status, Body
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
    summary="Show all tweets. ",
    tags=["Tweets"]
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
    summary="Post a new tweet. ",
    tags=["Tweets"]
)
def post_tweet(tweet: Tweet = Body(...)):
    """
    Posts a tweet in the app

    Parameters:
    - Request body parameters:
        - tweet: Tweet

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
        json.dump(results,f, default=str, indent=4)
        return tweet

### Show a tweet
@router.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet. ",
    tags=["Tweets"],
    deprecated=True
)
def show_tweet( 

):
    pass

### Delete a tweet
@router.delete(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet. ",
    tags=["Tweets"],
    deprecated=True
)
def delete_tweet( 

):
    pass

### Update a tweet
@router.put(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet. ",
    tags=["Tweets"],
    deprecated=True
)
def update_tweet( 

):
    pass
