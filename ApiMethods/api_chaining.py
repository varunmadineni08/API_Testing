import requests
import json

def test_api_chaining():
    url = "https://dummyjson.com/auth/login"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30
    }

    response = requests.post(url, json=payload, headers=headers)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    # Check response is OK before parsing
    assert response.status_code == 200, f"Login failed: {response.status_code}"

    response_json = response.json()
    token = response_json.get("accessToken")  # Safe access
    print(token)

    url2="https://dummyjson.com/auth/me"
    headers2={
        "Authorization":f"Bearer {token}"
    }
    response2=requests.get(url2,headers=headers2)
    print(response2.json())





