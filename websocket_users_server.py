import asyncio

import websockets
from websockets import ServerConnection


# Обработчик входящих сообщений
async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")  # Логируем поступившее сообщение
        # Генерируем пять последовательных сообщений с номером и текстом исходного сообщения
        responses = [
            f"{i + 1}. Сообщение пользователя: {message}" for i in range(5)
        ]

        # Отправляем каждому клиенту пять последовательных сообщений
        for resp in responses:
            await websocket.send(resp)

    


# Запуск WebSocket-сервера на порту 8765
async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())