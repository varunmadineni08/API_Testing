import requests
import json

url="https://automationexercise.com/api/searchProduct"
payload={
    "shirts":10,
    "pants":10,
    "tshirst":5
}
def test_post_request():
    response=requests.post(url,params=payload)
    assert response.status_code==200
    print(response.json())

