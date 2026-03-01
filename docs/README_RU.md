# 🚀 API Automation Framework (Python + Pytest)

## **[English](../README.md)** | **Русский**

**Этот проект создан в рамках обучения на курсе [«Автоматизация тестирования API с Python»](https://stepik.org/course/233196/info). Реализация тестового фреймворка для [qa-automation-engineer-api-course](https://github.com/Nikita-Filonov/qa-automation-engineer-api-course)**

[![API tests](https://github.com/lobanov-qa/autotests-api/actions/workflows/tests.yml/badge.svg)](https://github.com/lobanov-qa/autotests-api/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/python-3670A0?style=flat-square&logo=python&logoColor=ffdd54) ![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=flat-square&logo=pytest&logoColor=2f9fe3) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=flat-square&logo=git&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=flat-square&logo=githubactions&logoColor=white) 



---

## 🛠 В этой работе было реализовано

### Современный стек для тестирования API
- **Pytest** — фреймворк для написания тестов, работа с фикстурами и параметризацией.
- **HTTPX** — HTTP-клиент с поддержкой асинхронности, логирование запросов/ответов.
- **Pydantic** — валидация данных, работа с моделями запросов и ответов.
- **Swagger-coverage-tool** — отслеживание покрытия API по OpenAPI-спецификации.
- **Faker** — генерация правдоподобных тестовых данных.
- **Allure** — детальные отчёты с логированием и curl-командами.

---

### Практики, которые я освоил на курсе
- **Работать с Pytest** — фикстуры, маркеры, параметризация, плагины.
- **Тестировать REST API** — проверка ответов, обработка ошибок, авторизация.
- **Писать API-клиенты** для структурированного взаимодействия с эндпоинтами.
- **Организовывать тестовый код** — разделение на клиенты, тесты, утилиты, конфиги.
- **Настраивать Allure-отчёты** — аннотации, шаги, прикрепление логов и curl-команд.
- **Валидировать данные** — JSON Schema, кастомные ассерты.
- **Логирование HTTP-запросов** — автоматическая генерация curl-команд для отладки.

И другие продвинутые техники для повышения эффективности и надежности тестов.

Структура проекта следует отраслевым стандартам, чтобы обеспечить читаемость, поддерживаемость и масштабируемость тестового кода.

---



## 💡 Пример теста из проекта

```python
# Тест на обновление курса — пример структуры
@allure.story(AllureStory.UPDATE_ENTITY)
@allure.severity(Severity.CRITICAL)
def test_update_course(self, courses_client: CoursesClient, function_course: CourseFixture):
    request = UpdateCourseRequestSchema()
    response = courses_client.update_course_api(function_course.response.course.id, request)
    response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_update_course_response(request, response_data)
    validate_json_schema(response.json(), response_data.model_json_schema())
```


---


## 💡 Пример реализации клиента

```python
class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    @allure.step("Authenticate user")
    @tracker.track_coverage_httpx(f"{APIRoutes.AUTHENTICATION}/login")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"{APIRoutes.AUTHENTICATION}/login", json=request.model_dump(by_alias=True))
```


---

## 📁 Как устроен проект

Проект построен по **доменной структуре**, для поддержки чистого кода:

- `clients/` — API-клиенты для каждого сервиса (авторизация, курсы, пользователи…).
- `tests/` — тесты, сгруппированные по тем же доменам.
- `fixtures/` — фикстуры Pytest для подготовки данных.
- `tools/` — вспомогательные утилиты (Allure-конфиг, ассерты).
- `config.py` — настройки проекта и общие фикстуры.


---

## 🚀 Начало работы

> ⚠️ **Важно:** проект тестирует учебную  платформу [qa-automation-engineer-api-course](https://github.com/Nikita-Filonov/qa-automation-engineer-api-course) которая должна быть запущенна локально

### Клонирование репозитория
Для начала работы клонируйте репозиторий проекта с помощью Git:
```bash
git clone https://github.com/lobanov-qa/autotests-api.git
cd autotests-api
```

### Создание виртуального окружения
Рекомендуется использовать виртуальное окружение для управления зависимостями проекта. Следуйте инструкциям для вашей операционной системы:

#### Linux / MacOS
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Установка зависимостей
После активации виртуального окружения установите зависимости проекта, перечисленные в `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Запуск тестов с генерацией Allure-отчета
Для запуска тестов и генерации Allure-отчета используйте следующую команду:
```bash
pytest -m "regression" --alluredir=./allure-results
```
Это выполнит все тесты в проекте и отобразит результаты в терминале.

### Просмотр Allure-отчета
После выполнения тестов вы можете сгенерировать и просмотреть Allure-отчет с помощью:
```bash
allure serve allure-results

---

## 📞 Контакты

Ищу возможность начать карьеру в автоматизации тестирования. Готов к тестовому заданию, код-ревью и собеседованиям.

- **GitHub:** [lobanov-qa](https://github.com/lobanov-qa)
- **LinkedIn:** [evgenii-lobanov-qa](https://www.linkedin.com/in/evgenii-lobanov-qa/)
- **Telegram:** [lobanov_e_i](https://t.me/lobanov_e_i)


---


*Проект создан в рамках курса [«Автоматизация тестирования API с Python»](https://stepik.org/course/233196/info) (автор — Никита Филонов).*  

