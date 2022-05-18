import requests     

endpoint = "http://localhost:8000/api/products/"
data = {
    "title": "Pollito con papas",
    "price": 35.60
}
get_response = requests.post(endpoint, json=data)

print(get_response.json())
