import pytest
import copy
from api_client import ApiClient
from helpers import generate_user

@pytest.fixture()
def clear():
    user = generate_user()
    client = ApiClient()
    response = client.user_creation(user)
    assert response.status_code ==200 
    token =response.json()['accessToken']
    user = copy.deepcopy(user)
    try:
        yield user, token
    finally:
        client.user_delete(token) 

