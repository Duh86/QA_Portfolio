def get_kit_header(auth_token):
    return {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {auth_token}"
    }


user_header = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Анатолий",
    "phone": "+79995553322",
    "address": "г. Москва, ул. Пушкина, д. 10"
}

