import pytest
import requests
import copy
from constant import url, user_creation, user_delete
from helpers import generate_user

@pytest.fixture()
def clear():
    user = generate_user()
    response = requests.post(url + user_creation, json=user)
    assert response.status_code ==200 ,f'регистрация не удалась {response.text}'
    token =response.json()['accessToken']
    user = copy.deepcopy(user)
    yield user 
    requests.delete(url + user_delete, headers={'Authorization': token}) 


