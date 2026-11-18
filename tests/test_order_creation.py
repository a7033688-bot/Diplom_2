import allure
import requests
from constant import url, user_authorization, data_about_ingredient, order_cretion


class TestOrderCreation:

    @allure.title('создание заказа авторизированным пользователе с продуктами и правильным хешем')
    def test_creating_an_order_by_an_authorized_user_with_ingredients_that_have_correct_hash(self,clear):
        user = clear
        del user['name']
        requests.post(url + user_authorization,json=user)
        response = requests.get(url + data_about_ingredient)
        r = response.json()
        burger = {"ingredients":[r['data'][0]['_id'],r['data'][1]['_id']]}
        order = requests.post(url + order_cretion, json=burger)
        assert 'true' in order.text and order.status_code == 200

    @allure.title('создание заказа авторизированным пользователе с продуктами и неправильным хешем')
    def test_creating_an_order_by_an_authorized_user_with_ingredients_that_have_incorrect_hash(self,clear):
        user = clear
        del user['name']
        requests.post(url + user_authorization,json=user)
        response = requests.get(url + data_about_ingredient)
        r = response.json()
        burger = {"ingredients":["111111111","222222222"]}
        order = requests.post(url + order_cretion, json=burger)
        assert order.status_code == 500

    @allure.title('создание заказа авторизированным пользователе без продуктов')
    def test_creating_an_order_for_an_authorized_user_without_any_ingredients(self,clear):
        user = clear
        del user['name']
        requests.post(url + user_authorization,json=user)
        response = requests.get(url + data_about_ingredient)
        r = response.json()
        burger = {"ingredients":[]}
        order = requests.post(url + order_cretion, json=burger)
        assert 'false' in order.text and order.status_code == 400

    @allure.title('создание заказа не авторизированным пользователе с продуктами и правильным хешем')
    def test_creating_an_order_by_an_unauthorized_user_with_ingredients_that_have_correct_hash(self):
        response = requests.get(url + data_about_ingredient)
        r = response.json()
        burger = {"ingredients":[r['data'][0]['_id'],r['data'][1]['_id']]}
        order = requests.post(url + order_cretion, json=burger)
        assert 'false' in order.text and order.status_code == 401, f'Заказ оформлен не авторизированным пользователем'

    @allure.title('создание заказа неавторизированным пользователе с продуктами и неправильным хешем')
    def test_creating_an_order_by_an_unauthorized_user_with_ingredients_that_have_incorrect_hash(self):
        response = requests.get(url + data_about_ingredient)
        r = response.json()
        burger = {"ingredients":["111111111","222222222"]}
        order = requests.post(url + order_cretion, json=burger)
        assert order.status_code == 500, f'Заказ получилось оформить не авторизированному пользователю с неправильным хешом продуктов'

    @allure.title('создание заказа неавторизированным пользователе с без продуктами')
    def test_creating_an_order_for_an_unauthorized_user_without_any_ingredients(self):
        response = requests.get(url + data_about_ingredient)
        r = response.json()
        burger = {"ingredients":[]}
        order = requests.post(url + order_cretion, json=burger)
        assert 'false' in order.text and order.status_code == 400, 'Заказ получилось оформить не авторизированному пользователю без продуктов'
        