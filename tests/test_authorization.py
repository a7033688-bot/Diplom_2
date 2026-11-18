import allure
import requests
from constant import url, user_authorization


class TestAuthorization:

    @allure.title('вход под существующим пользователем')
    def test_log_in_as_an_existing_user(self,clear):
        user = clear
        del user['name']
        response = requests.post(url + user_authorization,json=user)
        assert response.status_code == 200 and 'true' in response.text

    @allure.title('вход с неверным логином и паролем')
    def test_log_in_with_incorrect_login_and_password(self,clear):
        user = clear
        user['email'] = 'dddd@mail.ru'
        user['password'] = '11111'
        response = requests.post(url + user_authorization,json=user)
        assert response.status_code == 401 and 'false' in response.text