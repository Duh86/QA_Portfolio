import requests
from tests.configuration import get_full_URL, PET_BY_STATUS_URL

def get_pets_by_status(status_value):
    if isinstance(status_value, str):
        params = {"status": status_value}
    else:
        params = status_value
    return requests.get(get_full_URL(PET_BY_STATUS_URL), params=params)