from pydantic import BaseModel
from datetime import datetime
from pydantic import EmailStr

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id : int
    created_add : datetime

    class Config():
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_add: datetime

    class Config():
        orm_mode = True