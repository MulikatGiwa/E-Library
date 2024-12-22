from fastapi.testclient import TestClient
from app.main import app
from app.crud.users import User
from unittest.mock import patch

client = TestClient(app)

Mock_Users : dict[int, User] = {
    1: User(id=1, name="Muli", email="muli@muli.com", password="muli123", is_active=True),
    2: User(id=2, name="Ade", email="ade@ade.com", password="ade243", is_active=True),
    3: User(id=3, name="Bimpe", email="bimpe@bimpe.com", password="bimpe456", is_active=True),
    4: User(id=4, name="John", email="john@john.com", password="john231", is_active=True),
    5: User(id=5, name="Sum", email="sum@sum.com", password="sum765", is_active=True)
  }

@patch("app.crud.users.Users", Mock_Users)
def test_signup():
  new_user = {
    "user": {
      "name": "Zay",
      "email" : "zay@gmail.com",
      "password" : "zay423"
    },
    "confirm_password" : "zay423"
    }


  test_new_user = {
      "name": "Zay",
      "email": "zay@gmail.com",
      "password": "zay423",
      "id": len(Mock_Users)+1,
      "is_active": True
    }

  response = client.post("/signup", json=new_user)
  assert response.status_code == 201
  assert response.json()["data"] == test_new_user
  assert response.json()["message"] == "Signup Successful"

@patch("app.crud.users.Users", Mock_Users)
def test_login():

  user_data = {
    "email" : "muli@muli.com",
    "password" : "muli123"
    }
  
  response = client.post("/login", json=user_data)
  assert response.status_code == 200
  assert response.json()["message"] == "Login Successful"

@patch("app.crud.users.Users", Mock_Users)
def test_get_users():

  response = client.get("/users")

  assert response.status_code ==200
  test_mock_users = {str(key):values.model_dump() for key, values in Mock_Users.items()}
  assert response.json()["data"] == test_mock_users
  assert response.json()["message"] == "Successful"

@patch("app.crud.users.Users", Mock_Users)
def test_get_users_by_id():

  test_user_data = {
      "name": "Muli",
      "email": "muli@muli.com",
      "password": "muli123",
      "id": 1,
      "is_active": True
  }
  response = client.get("/users/1")
  assert response.status_code == 200
  assert response.json()["data"] == test_user_data
  assert response.json()["message"] == "Successful"

@patch("app.crud.users.Users", Mock_Users)
def test_update_user():

  user_update = {
    "name": "Mulikat",
    "email": "muli@muli.com",
    "password": "muli123"
  }

  test_user_update = {
      "name": "Mulikat",
      "email": "muli@muli.com",
      "password": "muli123",
      "id": 1,
      "is_active": True
  }

  response = client.put("/users/1", json=user_update)
  assert response.status_code == 200
  assert response.json()["data"] == test_user_update 
  assert response.json()["message"] == "User Updated Successfully"

@patch("app.services.users.Users", Mock_Users)
def test_deactivate_user():

  response = client.patch("/users/2")
  assert response.status_code == 200
  assert response.json()["message"] == "User Deactivated Successfully"

@patch("app.crud.users.Users", Mock_Users)
def test_delete_user():

  response = client.delete("/users/3")
  assert response.status_code == 200
  assert response.json()["message"] == "User Deleted Successfully"