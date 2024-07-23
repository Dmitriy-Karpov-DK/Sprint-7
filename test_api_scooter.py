import requests
import pytest
import allure
from constants import Constants
from method_api_scooter import MethodApi
from data_modules import DataResponse, Data


@allure.description('Тесты на ручку POST/api/v1/courier')
class TestCreateCourier:

    @allure.title('Проверим создание курьера')
    def test_create_courier_input_positive_data_successful(self):
        login = Constants.LOGIN
        password = Constants.PASSWORD
        first_name = Constants.FIRSTNAME
        response = MethodApi.create_courier(self, login, password, first_name)
        assert response.status_code == 201
        assert response.json() == {'ok': True}
        MethodApi.delete_courier(self, login, password)

    @allure.title('Проверяем что повторно нельзя создать курьера с тем же логином')
    def test_re_create_identical_couriers_show_error(self):
        login = Constants.LOGIN
        password = Constants.PASSWORD
        first_name = Constants.FIRSTNAME
        response = MethodApi.create_courier(self, login, password, first_name)
        assert response.status_code == 201
        response = MethodApi.create_courier(self, login, password, first_name)
        assert response.status_code == 409
        assert DataResponse.data_response_login_already_in_use in response.json()['message']
        MethodApi.delete_courier(self, login, password)

    @allure.title('Проверим что создание курьера возможно только при заполнении обязательных полей')
    def test_create_courier_no_required_fields_show_error(self):
        login = Constants.LOGIN
        password = Constants.PASSWORD
        response = requests.post(Constants.URL_CREATE_COURIER, data={"login": "", "password": password})
        assert response.status_code == 400
        res = response.json()
        assert res["message"] == DataResponse.data_response_not_data_to_create
        response = requests.post(Constants.URL_CREATE_COURIER, data={"login": login, "password": ""})
        assert response.status_code == 400
        res = response.json()
        assert res["message"] == DataResponse.data_response_not_data_to_create


@allure.description('Тесты на ручку POST/api/v1/courier/login')
class TestLoginCourier:

    @allure.title('Проверим что курьер может авторизоваться')
    def test_login_courier_successful(self):
        login = Constants.LOGIN
        password = Constants.PASSWORD
        first_name = Constants.FIRSTNAME
        MethodApi.create_courier(self, login, password, first_name)
        response = MethodApi.auth_courier(self, login, password)
        assert response.status_code == 200
        assert type(response.json()['id']) is int
        MethodApi.delete_courier(self, login, password)

    @allure.title('Проверим что курьер может авторизоваться только при заполнении обязательных полей')
    @pytest.mark.parametrize('logintest, passwordtest', [["", Constants.PASSWORD], [Constants.LOGIN, ""]])
    def test_login_courier_no_required_fields_show_error(self, logintest, passwordtest):
        login = Constants.LOGIN
        password = Constants.PASSWORD
        first_name = Constants.FIRSTNAME
        MethodApi.create_courier(self, login, password, first_name)
        response = requests.post(Constants.URL_LOGIN_COURIER, data={"login": logintest, "password": passwordtest})
        assert response.status_code == 400
        res = response.json()
        assert res["message"] == DataResponse.data_response_not_data_log_in
        MethodApi.delete_courier(self, login, password)

    @allure.title('Проверим что авторизация не возможна при неправильном логине или пароле')
    @pytest.mark.parametrize('logintest, passwordtest', [["fake", Constants.PASSWORD], [Constants.LOGIN, "0001"]])
    def test_login_courier_invalid_password_or_login_show_error(self, logintest, passwordtest):
        login = Constants.LOGIN
        password = Constants.PASSWORD
        first_name = Constants.FIRSTNAME
        MethodApi.create_courier(self, login, password, first_name)
        response = requests.post(Constants.URL_LOGIN_COURIER, json={
            'login': logintest, 'password': passwordtest})
        assert response.status_code == 404
        assert response.json()["message"] == DataResponse.data_response_account_not_found
        MethodApi.delete_courier(self, login, password)


@allure.description('тесты на ручку POST/api/v1/orders')
class TestCreateOrder:


    @allure.title('Проверим правильность заказа при выборе цвета самоката')
    @pytest.mark.parametrize('colors', [["BLACK"], ["GREY"], [""], ["BLACK", "GREY"]])
    def test_choose_color_scooter_create_order_successful(self, colors):
        data_order = Data.data_order
        data_order["color"] = colors

        response = requests.post(Constants.URL_CREATE_ORDER, json=data_order)
        assert response.status_code == 201
        assert 'track' in response.json()


@allure.description('Тесты на ручку GET/api/v1/orders')
class TestListOrders:

    @allure.title('Проверим получение списка заказов')
    def test_get_list_orders_show_list(self):
        response = requests.get(Constants.URL_GET_LIST_ORDERS).json()
        assert "orders" in response


@allure.description('Тесты на ручку DELETE/api/v1/courier/')
class TestDeleteCourier:

    @allure.title('Проверим удаление курьера')
    def test_deleted_courier_successful(self):
        login = Constants.LOGIN
        password = Constants.PASSWORD
        first_name = Constants.FIRSTNAME
        MethodApi.create_courier(self, login, password, first_name)
        response = MethodApi.delete_courier(self, login, password)
        assert response.status_code == 200
        assert response.json() == {'ok': True}
        res = MethodApi.auth_courier(self, login, password)
        assert res.json()["message"] == DataResponse.data_response_account_not_found
