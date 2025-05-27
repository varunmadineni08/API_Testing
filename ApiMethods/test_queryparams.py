import requests

def test_query_params():
    url="https://reqres.in/api/users"
    parameter={
        "page":"2"
    }

    response=requests.get(url,params=parameter)
    assert response.status_code==200