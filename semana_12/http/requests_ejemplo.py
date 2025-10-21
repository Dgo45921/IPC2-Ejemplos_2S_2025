import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print("Código de estado:", response.status_code)
print("Encabezados:", response.headers["Content-Type"])
print("JSON:", response.json())
