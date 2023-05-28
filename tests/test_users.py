from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app
from app import schemas
from app.config import Settings
from app.database import get_db
from app.database import Base
import pytest

settings = Settings()


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine) #drop tables
    Base.metadata.create_all(bind=engine) #create tables"
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


def test_root(client):
    res = client.get("/")
    assert (res.json().get("message")) == "Hello World"
    assert res.status_code == 200

def test_create_user(client):
    res = client.post("/users/", json={
        "email": "test99@mail.com",
        "password": "test"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "test99@mail.com"


