from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True # Default value

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id : int
    created_add : datetime

    class Config():
        orm_mode = True

