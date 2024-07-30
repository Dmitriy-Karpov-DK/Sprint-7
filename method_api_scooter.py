import allure
import requests
from constants import Constants


class MethodApi:

    @allure.step('Создаем курьера')
    def create_courier(self, login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(Constants.URL_CREATE_COURIER, json=payload)
        return response

    @allure.step('Авторизация курьера')
    def auth_courier(self, login, password):
        response = requests.post(Constants.URL_LOGIN_COURIER, json={
            'login': login, 'password': password})
        return response

    @allure.step('Получаем id курьера')
    def get_id(self, login, password):
        response = requests.post(Constants.URL_LOGIN_COURIER, json={
            'login': login, 'password': password}).json()
        return response['id']

    @allure.step('Удаляем курьера')
    def delete_courier(self, login, password):
        id_courier = requests.post(Constants.URL_LOGIN_COURIER, json={
            'login': login, 'password': password}).json()
        response = requests.delete(f'{Constants.URL_DELETE_COURIER}{id_courier['id']}')
        return response
