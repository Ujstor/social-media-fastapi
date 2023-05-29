from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app import schemas
from app.config import Settings
from app.database import get_db
from app.database import Base
import pytest
from app.oauth2 import create_access_token
from app import models

settings = Settings()


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine) #drop tables
    Base.metadata.create_all(bind=engine) #create tables"
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

@pytest.fixture
def test_user(client):
    user_data = {"email": "ujstor@gmail.com",
                "password": "password123"}
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user

@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user["id"]})

@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    return client

@pytest.fixture
def test_post(test_user, session):
    post_data = [{
        "title": "Test Post",
        "content": "Test Content",
        "owner_id": test_user["id"]
    }, {
        "title": "Test Post 2",
        "content": "Test Content 2",
        "owner_id": test_user["id"]
    }, {
        "title": "Test Post 3",
        "content": "Test Content 3",
        "owner_id": test_user["id"]
    }]

    def create_post_model(post):
        return models.Post(**post)

    post_map = map(create_post_model, post_data)
    posts = list(post_map)

    session.add_all(posts)
    session.commit()
    posts = session.query(models.Post).all()
    return posts
