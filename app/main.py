from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, users, auth, vote
from .config import Settings
from fastapi.middleware.cors import CORSMiddleware

settings = Settings()

#models.Base.metadata.create_all(bind=engine)
#using alembic instead

app = FastAPI()

origins = ["https://www.google.com"] #or ["*"] for all origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World"}