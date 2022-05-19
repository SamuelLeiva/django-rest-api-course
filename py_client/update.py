import requests     

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "Hello World my old friend",
    "price": 124.57
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())
