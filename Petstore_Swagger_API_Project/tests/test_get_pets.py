import pytest
import requests
from tests.sender_stand_request import get_pets_by_status
from tests.configuration import PET_BY_STATUS_URL, get_full_URL

    #-------------------Вспомогательная функция для проверки status в запросе = status в ответе--#
def extract_expected_statuses(value):
    if isinstance(value, str):
        return set(value.split(","))
    return {v for k, v in value if k == "status"}

    #-------------------Позитивные проверки, status - множественный параметр---------------------#

@pytest.mark.parametrize("params", [
    [("status", "available"), ("status", "pending"), ("status", "sold")],
    [("status", "available"), ("status", "pending")],
    [("status", "available"), ("status", "sold")],
    [("status", "available")],
    [("status", "pending"), ("status", "sold")],
    [("status", "pending")],
    [("status", "sold")]
])


def test_get_pets_by_status_positive_1(params): 
    response = get_pets_by_status(params)
    expected_statuses = extract_expected_statuses(params)

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(pet.get("status") in expected_statuses for pet in response.json())

    #-----------------Позитивные проверки, status - строка--------------------------------------#

@pytest.mark.parametrize("value", [
    "available,pending,sold",
    "available,pending",
    "available,sold",
    "available",
    "pending,sold",
    "pending",
    "sold"
])

def test_get_pets_by_status_positive_2(value): 
    response = get_pets_by_status(value)
    expected_statuses = extract_expected_statuses(value)

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(pet.get("status") in expected_statuses for pet in response.json())

    #-----------------Негативные проверки------------------------------------------------------#

@pytest.mark.xfail(reason="API некорректно возвращает код 200 при вводе в статусе невалидных значений")
@pytest.mark.parametrize("invalid_value",[
    "",
    "frozen",
    "1",
    "Продано",
    "!№?",
    " ",
])

def test_get_pets_by_status_negative(invalid_value):
    response = get_pets_by_status(invalid_value)

    try:
        print(response.json())
    except Exception:
        print("Не JSON", response.text)

    assert response.status_code == 400
    assert "Invalid" in response.text

    #----------------Негативаня проверка, без передачи параметра status-----------------------#

@pytest.mark.xfail(reason="API некорректно возвращает код 200 при запросе без указания status")
def test_get_pets_by_status_negative_no_param():
    url = get_full_URL(PET_BY_STATUS_URL)
    response = requests.get(url)

    assert response.status_code == 400