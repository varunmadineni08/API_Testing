import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError


def test_validate_jsonscehma():
    url="https://dummyjson.com/users/1"
    response=requests.get(url)
    assert response.status_code==200
    print(response.json())
    data=response.json()

    # Step 2: Define the expected JSON schema
    schema={
        "type" : "object",
        "required" : ["id","firstName","lastName","age","email","gender","phone"],
        "properties" : {
            "id": {"type":"integer"},
            "fisrtName": {"type":"string"},
            "lastName": {"type":"string"},
            "age":{"type":"integer"},
            "email":{"type":"string", "format": "email"},
            "gender":{"type":"string"},
            "phone":{"type":"string"}

        }
    }

    try:
        validate(instance=data,schema=schema)
        print("validation succeeded")
    except ValidationError as e:
        print("validation Error")
        print(f"error message {e.message}")

