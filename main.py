from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}

@app.post("/create-post")
def create_post(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title: {payLoad['title']} content: {payLoad['content']}"}