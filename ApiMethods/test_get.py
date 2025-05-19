import requests
import json

base_url="https://reqres.in/"
end_point="api/users?page=2"
url=base_url+end_point

def test_get_request():
    response=requests.get(url)
    assert response.status_code==200
    print(response.json())