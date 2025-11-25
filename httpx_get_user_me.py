import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
login_payload = {
    "email": "test@example.com",
    "password": "123456"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()


# Формируем payload для авторизации
access_payload = login_response_data["token"]["accessToken"]


# Передача заголовков
headers = {"Authorization": f"Bearer {access_payload}"}

# Выполняем запрос на получение данных о пользователе
response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

# Выводим в консоль ответ с данными о пользователе и статус код
print(response.json())
print(response.status_code)