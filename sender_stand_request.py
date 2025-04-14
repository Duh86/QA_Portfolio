import requests
import configuration
import data

def get_new_user_token(body):
    response = requests.post(configuration.get_full_url(configuration.USER_CREATING),
                             headers = data.user_header,
                             json = body)
    return response.json()["authToken"]


def post_new_client_kit(kit_body, auth_token):
    headers = data.get_kit_header(auth_token)
    response = requests.post(configuration.get_full_url(configuration.KIT_CREATING),
                             headers = headers,
                             json = kit_body,
                            )
    return response