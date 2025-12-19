import requests

BASE_URL = "http://localhost:5000"

def test_get_objects():
    response = requests.get(f"{BASE_URL}/api/objects")
    assert response.status_code == 200
    objects = response.json()
    assert isinstance(objects, list)
    assert len(objects) >= 0

def test_add_and_get_object():
    new_obj = {
        "name": "Тестовая Планета",
        "type": "Планета",
        "constellation": "Тест",
        "distance_ly": 10
    }
    response = requests.post(f"{BASE_URL}/api/objects", json=new_obj)
    assert response.status_code == 201
    created = response.json()
    assert created["name"] == "Тестовая Планета"

    # Получаем по ID
    obj_id = created["id"]
    response = requests.get(f"{BASE_URL}/api/objects/{obj_id}")
    assert response.status_code == 200
    retrieved = response.json()
    assert retrieved["name"] == "Тестовая Планета"

def test_delete_object():
    new_obj = {
        "name": "Объект для удаления",
        "type": "Астероид",
        "constellation": "Тест",
        "distance_ly": 1
    }
    response = requests.post(f"{BASE_URL}/api/objects", json=new_obj)
    assert response.status_code == 201
    obj_id = response.json()["id"]

    response = requests.delete(f"{BASE_URL}/api/objects/{obj_id}")
    assert response.status_code == 200

    response = requests.get(f"{BASE_URL}/api/objects/{obj_id}")
    assert response.status_code == 404