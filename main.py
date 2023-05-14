from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True # Default value
    rating: Optional[int] = None # Optional value

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}

@app.post("/create-post")
def create_post(post: Post):
    print(post) # Convert to model
    print(post.dict()) # Convert to dictionary
    return {"data": "Post is created successfully"}
