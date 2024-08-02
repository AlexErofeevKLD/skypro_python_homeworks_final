import pytest
import requests
from Lesson_8.constants import x_clients_URL

@pytest.fixture()
def get_token(username='raphael', password='cool-but-crude'):
    log_pass = {'username': username, 'password': password}
    resp_token = requests.post(x_clients_URL + '/auth/login', json=log_pass)
    token = resp_token.json()['userToken']
    return token
