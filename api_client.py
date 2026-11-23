import allure
import requests
from constant import Url


class ApiClient:

    @allure.step('создание пользователя ')
    def user_creation(self,clear):
        user = clear
        response = requests.post(Url.url + Url.user_creation, json=user)
        return response

    @allure.step('удаление пользователя ')
    def user_delete(self,clear):
        token = clear
        response = requests.delete(Url.url + Url.user_delete,
                                   headers={'Authorization': token})
        return response

    @allure.step('авторизация пользователя ')
    def user_autorization(self,clear):
        user = clear
        response = requests.post(Url.url + Url.user_authorization,json= user)
        return response

    @allure.step('получение ингредиентов')
    def obtaining_data_about_an_ingredient(self):
        response = requests.get(Url.url + Url.data_about_ingredient)
        return response
    
    @allure.step('заказ бургера')
    def order_creation(self,burger,clear=''):
        token = clear
        response = requests.post(Url.url + Url.order_cretion,json=burger,
                                 headers={'Authorization': token})
        return response