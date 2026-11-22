import allure
from api_client import ApiClient
from helpers import generate_user

class TestUserCreation:
    
    @allure.title('создание уникального пользователя')
    def test_user_creation(self):
        client = generate_user()
        user = ApiClient()
        response = user.user_creation(client)
        token = response.json()['accessToken']
        response = user.user_delete(token)
        assert response.status_code == 202

    @allure.title('создание пользователя который уже зарегистрирован')
    def test_create_user_who_is_already_registered(self,clear):
        user, token = clear
        client = ApiClient()
        response = client.user_creation(user)
        assert response.status_code == 403 and 'User already exists' in response.text

    @allure.title('создать пользователя и не заполнить одно из обязательных полей')
    def test_create_user_without_required_field(self,clear):
        user, token = clear
        del user['email']
        client = ApiClient()
        response = client.user_creation(user)
        assert response.status_code == 403 and 'Email, password and name are required fields' in response.text