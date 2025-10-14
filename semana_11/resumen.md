# Flask HTTP Response Codes API

Esta aplicación Flask muestra ejemplos prácticos de **todas las categorías de códigos de estado HTTP** (1xx, 2xx, 3xx, 4xx, 5xx).

---

## 1xx - Informational
Respuestas informativas. No se usan comúnmente en APIs REST.

| Código | Ruta | Descripción |
|--------|------|-------------|
| 100 | `/continue` | Indica que el cliente debe continuar con la petición. |
| 101 | `/switching_protocols` | El servidor cambia de protocolo. |

---

## 2xx - Success
El servidor procesó la petición correctamente.

| Código | Ruta | Descripción |
|--------|------|-------------|
| 200 | `/ok` | Respuesta exitosa estándar. |
| 201 | `/created` | Recurso creado correctamente. |
| 202 | `/accepted` | Petición aceptada, procesándose. |
| 204 | `/no_content` | Éxito sin contenido en la respuesta. |

---

## 3xx - Redirection
El cliente debe seguir una redirección.

| Código | Ruta | Descripción |
|--------|------|-------------|
| 301 | `/moved_permanently` | Recurso movido permanentemente. |
| 302 | `/found` | Redirección temporal. |
| 303 | `/see_other` | Usa GET para acceder al nuevo recurso. |
| 304 | `/not_modified` | Recurso no modificado (usado con cache). |
| 307 | `/temporary_redirect` | Redirección temporal, método conservado. |
| 308 | `/permanent_redirect` | Redirección permanente, método conservado. |

---

## 4xx - Client Errors
Errores por parte del cliente.

| Código | Ruta | Descripción |
|--------|------|-------------|
| 400 | `/bad_request` | Petición malformada. |
| 401 | `/unauthorized` | Autenticación requerida. |
| 403 | `/forbidden` | Acceso denegado. |
| 404 | `/not_found` | Recurso no encontrado. |
| 405 | `/method_not_allowed` | Método HTTP no permitido. |
| 409 | `/conflict` | Conflicto en el estado del recurso. |
| 410 | `/gone` | El recurso ya no está disponible. |
| 422 | `/unprocessable_entity` | Error de validación o formato inválido. |
| 429 | `/too_many_requests` | Demasiadas peticiones. |

---

## 5xx - Server Errors
Errores en el servidor.

| Código | Ruta | Descripción |
|--------|------|-------------|
| 500 | `/internal_error` | Error interno del servidor. |
| 501 | `/not_implemented` | Endpoint no implementado. |
| 502 | `/bad_gateway` | Error en la pasarela. |
| 503 | `/service_unavailable` | Servicio no disponible. |
| 504 | `/gateway_timeout` | Tiempo de espera agotado. |

---

## Manejadores Globales

El archivo incluye *error handlers* personalizados:

```python
@app.errorhandler(404)
def handle_404(e):
    return jsonify(error="Custom handler: Resource not found"), 404
