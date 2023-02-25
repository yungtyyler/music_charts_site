import requests

ENDPOINT = ""


def test_an_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_create_user():
    response = requests.put(ENDPOINT + '')

# Need to do more research on how to integrate these tests