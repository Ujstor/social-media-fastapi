from app import schemas

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
    res = client.get(f"/posts/[0].id")
    assert res.status_code == 401

def test_get_one_post_not_exist(authorized_client, test_post):
    res = authorized_client.get("/posts/9999999")
    assert res.status_code == 404

