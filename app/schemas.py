from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
from pydantic import EmailStr
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config():
        orm_mode = True

class Post(PostBase):
    id : int
    created_at : datetime
    owner_id : int
    owner : UserOut
    class Config():
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config():
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id : Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: int

    @validator('dir')
    def post_id_must_be_zero_or_one(cls, v):
        if v not in [0, 1]:
            raise ValueError('Input 1 for upvote or 0 for downvote')
        return v