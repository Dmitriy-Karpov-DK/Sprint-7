import random


class Constants:
    LOGIN = f"dksprint7v{random.randint(10000, 99999)}"
    PASSWORD = "1234"
    FIRSTNAME = "dksprint7"
    URL_LOGIN_COURIER = "https://qa-scooter.praktikum-services.ru/api/v1/courier/login"
    URL_CREATE_COURIER = "https://qa-scooter.praktikum-services.ru/api/v1/courier"
    URL_DELETE_COURIER = "https://qa-scooter.praktikum-services.ru/api/v1/courier/"
    URL_CREATE_ORDER = "https://qa-scooter.praktikum-services.ru/api/v1/orders"
    URL_GET_LIST_ORDERS = "https://qa-scooter.praktikum-services.ru/api/v1/orders"
