import allure
import requests
from constant import url,user_creation,user_delete
from helpers import generate_user


class TestUserCreation:
    
    @allure.title('создание уникального пользователя')
    def test_user_creation(self):
        user = generate_user()
        response = requests.post(url + user_creation, json=user)
        assert response.status_code == 200 and 'accessToken' in response.text
        token = response.json()['accessToken']
        requests.delete(url + user_delete, headers={'Authorization': token})

    @allure.title('создание пользователя который уже зарегистрирован')
    def test_create_user_who_is_already_registered(self,clear):
        user = clear
        response = requests.post(url + user_creation, json=user)
        assert response.status_code == 403 and 'User already exists' in response.text

    @allure.title('создать пользователя и не заполнить одно из обязательных полей')
    def test_create_user_without_required_field(self,clear):
        user = clear
        del user['email']
        response = requests.post(url + user_creation, json=user)
        assert response.status_code == 403 and 'Email, password and name are required fields' in response.text