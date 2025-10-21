import urllib.request
import urllib.parse
import json

url = "https://jsonplaceholder.typicode.com/posts"

# Datos a enviar (formato dict)
payload = {"title": "Nuevo Post", "body": "Contenido del post", "userId": 1}

# Convertimos a JSON y luego a bytes
data = json.dumps(payload).encode("utf-8")

# Definimos la solicitud HTTP manualmente
req = urllib.request.Request(
    url,
    data=data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

# Ejecutamos la petición
with urllib.request.urlopen(req) as response:
    res = response.read().decode("utf-8")
    print("Código de estado:", response.status)
    print("Respuesta:", res)
