from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True # Default value
    rating: Optional[int] = None # Optional value

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "title of post 2", "content": "content of post 2", "id": 2}
            ]

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(1, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}") # id is a path parameter
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found")
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} dose not exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} dose not exist")

    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict

    return {"data": post_dict}

