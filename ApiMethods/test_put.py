def test_put_user():
    import requests

    url = "https://reqres.in/api/users/2"
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "reqres-free-v1"
    }

    response = requests.put(url, json=payload, headers=headers)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    print("Response JSON:", response.json())

