from app import schemas
from .database import client, session


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
    assert res.status_code == 201

def test_login_user(client):
    res = client.post("/login", data={
        "username": "test99@mail.com",
        "password": "test"})
    print(res.json())
    assert res.status_code == 200
    #bad practice, this test is dependent on the previous test


