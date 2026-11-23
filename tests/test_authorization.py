import allure
from api_client import ApiClient


class TestAuthorization:

    @allure.title('вход под существующим пользователем')
    def test_log_in_as_an_existing_user(self,clear):
        user, token = clear
        client = ApiClient()
        response = client.user_autorization(user)
        assert response.status_code == 200 and 'true' in response.text

    @allure.title('вход с неверным логином и паролем')
    def test_log_in_with_incorrect_login_and_password(self):
        user = {}
        user['email'] = 'uiuiui@mail.ru'
        user['password'] = '65885'
        client = ApiClient()
        response = client.user_autorization(user)
        assert response.status_code == 401 and 'false' in response.text