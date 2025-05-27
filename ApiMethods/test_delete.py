import requests

def test_delete():

    url="https://reqres.in/api/users/2"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "reqres-free-v1"
    }
    response=requests.delete(url,headers=headers)
    assert response.status_code==204,f"unidentified statuscode{response.status_code}"
