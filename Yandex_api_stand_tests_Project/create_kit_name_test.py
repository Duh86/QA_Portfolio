import configuration
import data
import sender_stand_request
import requests

auth_token = sender_stand_request.get_new_user_token(data.user_body)

def get_kit_body(name):
    return {
    "name": name
    }


def positive_assert(kit_body, auth_token):
   response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
   assert response.status_code == 201
   assert response.json()["name"] == kit_body["name"]


def negative_assert_code_400(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

#ТЕСТЫ

def test_create_kit_name_one_char():
    kit_body = get_kit_body("а")
    positive_assert(kit_body, auth_token)

def test_create_kit_name_511_chars():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body, auth_token)

def test_create_kit_name_0_chars():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body, auth_token)

def test_create_kit_name_512_chars():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body, auth_token)

def test_create_kit_name_english_chars():
    kit_body = get_kit_body("QWErty")
    positive_assert(kit_body, auth_token)

def test_create_kit_name_russian_chars():
    kit_body = get_kit_body("Мария")
    positive_assert(kit_body, auth_token)

def test_create_kit_special_chars():
    kit_body = get_kit_body('"№%@",')
    positive_assert(kit_body, auth_token)

def test_create_kit_space():
    kit_body = get_kit_body("Человек и КО")
    positive_assert(kit_body, auth_token)

def test_create_kit_numbers_as_str():
    kit_body = get_kit_body("123")
    positive_assert(kit_body, auth_token)

def test_create_kit_no_params():
    negative_assert_code_400({}, auth_token)

def create_kit_number_type():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body, auth_token)

tests = [
    ("Допустимое количество символов (1)", test_create_kit_name_one_char),
    ("допустимое количество символов(511)", test_create_kit_name_511_chars),
    ("Количество символов меньше допустимого(0)", test_create_kit_name_0_chars),
    ("Количество символов больше допустимого (512)", test_create_kit_name_512_chars),
    ("Разрешены английские буквы", test_create_kit_name_english_chars),
    ("Разрешены русские буквы", test_create_kit_name_russian_chars),
    ("Разрешены спецсимволы", test_create_kit_special_chars),
    ("Разрешены пробелы", test_create_kit_space),
    ("Разрешены цифры", test_create_kit_numbers_as_str),
    ("Параметр не передан в запросе", test_create_kit_no_params),
    ("Передан другой тип параметра (число)", create_kit_number_type),
]


if __name__ == "__main__":
    print("== Запуск тестов ==")
    for name, test_func in tests:
        try:
            test_func()
            print(f"✅ Тест пройден: {name}")
        except AssertionError as e:
            print(f"❌ Тест провален: {name}")
            print("   ↳ Ошибка:", e)
        except Exception as ex:
            print(f"❌ Ошибка выполнения в тесте: {name}")
            print("   ↳ Исключение:", ex)
    print("== Тестирование завершено ==")