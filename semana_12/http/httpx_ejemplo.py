import httpx
import asyncio
import time

def t():
    return f"{time.perf_counter() - start_time:5.2f}s"

async def fetch_post(client, post_id):
    print(f"{t()} → Iniciando petición {post_id}")
    r = await client.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    print(f"{t()} ↳ Petición {post_id} recibió respuesta, procesando...")
    await asyncio.sleep(2)  # Simula tiempo de espera
    print(f"{t()} ✔ Petición {post_id} completada")
    return r.json()

async def saludar():
    for i in range(10):
        print(f"{t()} HOLA {i+1}")
        await asyncio.sleep(0.5) 

async def main():
    global start_time
    start_time = time.perf_counter()

    print("Iniciando descargas asincrónicas...\n")

    async with httpx.AsyncClient() as client:
        # Creamos las tareas de las peticiones
        fetch_tasks = [asyncio.create_task(fetch_post(client, i)) for i in range(1, 6)]
        # Creamos la tarea de imprimir 'HOLA'
        saludo_task = asyncio.create_task(saludar())

        # Esperamos a que todas terminen
        results = await asyncio.gather(*fetch_tasks, saludo_task)

    print(f"\n{t()} Todas las peticiones completadas.\n")

  
    for post in results:
        print(post)

asyncio.run(main())
