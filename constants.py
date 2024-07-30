import random


class Constants:
    LOGIN = f"dksprint7v{random.randint(10000, 99999)}"
    PASSWORD = "1234"
    FIRSTNAME = "dksprint7"
    URL_SCOOTER = "https://qa-scooter.praktikum-services.ru"
    URL_LOGIN_COURIER = f"{URL_SCOOTER}/api/v1/courier/login"
    URL_CREATE_COURIER = f"{URL_SCOOTER}/api/v1/courier"
    URL_DELETE_COURIER = f"{URL_SCOOTER}/api/v1/courier/"
    URL_CREATE_ORDER = f"{URL_SCOOTER}/api/v1/orders"
    URL_GET_LIST_ORDERS = f"{URL_SCOOTER}/api/v1/orders"
