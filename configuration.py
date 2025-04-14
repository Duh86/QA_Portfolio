BASE_URL = "https://petstore.swagger.io/v2"
PET_BY_STATUS_URL = "/pet/findByStatus"

def get_full_URL(path):
    return f'{BASE_URL}{path}'