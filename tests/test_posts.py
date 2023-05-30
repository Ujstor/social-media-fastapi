from app import schemas
import pytest

def test_get_all_post(authorized_client, test_post):
    res = authorized_client.get("/posts/")
    # def validate(posts):
    #     return schemas.PostOut(**posts)
    # post_map = map(validate, res.json())
    # post_list = list(post_map)
    assert len(res.json()) == len(test_post)
    assert res.status_code == 200


def test_unauthorized_get_all_post(client, test_post):
    res = client.get("/posts/")
    assert res.status_code == 401


def test_unauthorized_get_one_post(client, test_post):
    res = client.get("/posts/[0].id")
    assert res.status_code == 401


def test_get_one_post_not_exist(authorized_client, test_post):
    res = authorized_client.get("/posts/9999999")
    assert res.status_code == 404


def test_get_one_post(authorized_client, test_post):
    res = authorized_client.get(f"/posts/{test_post[0].id}")
    assert res.status_code == 200
    post = schemas.PostOut(**res.json())
    assert post.Post.id == test_post[0].id
    assert post.Post.title == test_post[0].title
    assert post.Post.content == test_post[0].content


@pytest.mark.parametrize("title, content, published", [
("Test Post99", "Test Content99", True),
("Test Post88", "Test Content88", False),
("Test Post77", "Test Content77", True),
])
def test_create_post(authorized_client, test_user, title, content, published):
    res = authorized_client.post("/posts/", json={
        "title": title,
        "content": content,
        "published": published,
    })
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published


def test_create_post_default_published_true(authorized_client, test_user, test_post):
    res = authorized_client.post("/posts/", json={
        "title": "Random Title",
        "content": "Random Content"
    })
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == "Random Title"
    assert created_post.content == "Random Content"
    assert created_post.published == True


def test_unauthorized_user_create_post(client):
    res = client.post("/posts/", json={
        "title": "Random Title",
        "content": "Random Content"
    })
    assert res.status_code == 401

def test_unauthorized_user_delete_post(client, test_post, test_user):
    res = client.delete(f"/posts/{test_post[0].id}")
    assert res.status_code == 401

def test_delete_post(authorized_client, test_post, test_user):
    res = authorized_client.delete(f"/posts/{test_post[0].id}")
    assert res.status_code == 204

def test_delete_post_not_exist(authorized_client, test_user):
    res = authorized_client.delete("/posts/999999999")
    assert res.status_code == 404

def test_delete_other_user_post(authorized_client, test_post, test_user):
    res = authorized_client.delete(f"/posts/{test_post[3].id}")
    assert res.status_code == 403

def test_update_post(authorized_client, test_post, test_user):
    data = {
        "title": "Updated Title",
        "content": "Updated Content",
        "id": test_post[0].id
    }
    res = authorized_client.put(f"/posts/{test_post[0].id}", json=data)
    updated_post = schemas.Post(**res.json())
    assert res.status_code == 200
    assert updated_post.title == data["title"]
    assert updated_post.content == data["content"]
    assert updated_post.id == data["id"]

def test_update_post_not_exist(authorized_client, test_user):
    data = {
        "title": "Updated Title",
        "content": "Updated Content",
        "id": 999999999
    }
    res = authorized_client.put(f"/posts/{data['id']}", json=data)
    assert res.status_code == 404

def test_update_other_user_post(authorized_client, test_post, test_user, test_user2):
    data = {
        "title": "Updated Title",
        "content": "Updated Content",
        "id": test_post[3].id
    }
    res = authorized_client.put(f"/posts/{data['id']}", json=data)
    assert res.status_code == 403

def test_unauthorized_user_update_post(client, test_post, test_user):
    res = client.put(f"/posts/{test_post[0].id}")
    assert res.status_code == 401

