SERVICE_URL = "https://aa260870-e3b0-46f3-9c54-4543eb3af94f.serverhub.praktikum-services.ru"
USER_CREATING = "/api/v1/users"
KIT_CREATING = "/api/v1/kits"

def get_full_url(path):
    return f"{SERVICE_URL}{path}" 