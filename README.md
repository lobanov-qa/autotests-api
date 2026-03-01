# 🚀 API Automation Framework (Python + Pytest)

## **English** | **[Russian](docs/README_RU.md)**

**This project was created as part of the ["API Test Automation with Python" ](https://stepik.org/course/233196/info) course.  Implementation of a test framework for the [API Course Test Server](https://github.com/Nikita-Filonov/qa-automation-engineer-api-course)**

[![API tests](https://github.com/lobanov-qa/autotests-api/actions/workflows/tests.yml/badge.svg)](https://github.com/lobanov-qa/autotests-api/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/python-3670A0?style=flat-square&logo=python&logoColor=ffdd54) ![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=flat-square&logo=pytest&logoColor=2f9fe3) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=flat-square&logo=git&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=flat-square&logo=githubactions&logoColor=white) 

---

## 🛠 What was implemented in this project

### Modern stack for API testing
- **Pytest** — framework for writing tests, working with fixtures and parameterization.
- **HTTPX** — HTTP client with async support, request/response logging.
- **Pydantic** — data validation, working with request and response models.
- **Swagger-coverage-tool** — tracking API coverage against OpenAPI specifications.
- **Faker** — generation of realistic test data.
- **Allure** — detailed reports with logging and curl commands.

---

### Practices I mastered in the course
- **Working with Pytest** — fixtures, markers, parameterization, plugins.
- **Testing REST API** — response validation, error handling, authorization.
- **Writing API clients** for structured interaction with endpoints.
- **Organizing test code** — separation into clients, tests, utilities, configs.
- **Setting up Allure reports** — annotations, steps, attaching logs and curl commands.
- **Validating data** — JSON Schema, custom assertions.
- **HTTP request logging** — automatic generation of curl commands for debugging.

And other advanced techniques to improve test efficiency and reliability.

The project structure follows industry standards to ensure readability, maintainability, and scalability of test code.

---

## 💡 Test example from the project

```python
# Test for updating a course — example structure
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

## 💡 Example client implementation

```python
class AuthenticationClient(APIClient):
    """
    Client for working with /api/v1/authentication
    """

    @allure.step("Authenticate user")
    @tracker.track_coverage_httpx(f"{APIRoutes.AUTHENTICATION}/login")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Method performs user authentication.

        :param request: Dictionary with email and password.
        :return: Server response as httpx.Response object
        """
        return self.post(f"{APIRoutes.AUTHENTICATION}/login", json=request.model_dump(by_alias=True))
```

---

## 📁 Project structure

The project is built using a **domain structure** for clean code maintenance:

- `clients/` — API clients for each service (authentication, courses, users...).
- `tests/` — tests grouped by the same domains.
- `fixtures/` — Pytest fixtures for data preparation.
- `tools/` — helper utilities (Allure config, assertions).
- `config.py` — project settings and common fixtures.

---


## 🚀 Getting Started

> ⚠️ **Important:** the project tests the educational [qa-automation-engineer-api-course](https://github.com/Nikita-Filonov/qa-automation-engineer-api-course)  platform, which must be running locally.

### Clone the Repository

To get started, clone the project repository using Git:

```bash
git clone https://github.com/lobanov-qa/autotests-api.git
cd autotests-api
```

### Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies. Follow the instructions for your operating
system:

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

### Install Dependencies

Once the virtual environment is activated, install the project dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Running the Tests with Allure Report Generation

To run the tests and generate an Allure report, use the following command:

```bash
pytest -m "regression" --alluredir=./allure-results
```

This will execute all tests in the project and display the results in the terminal.

### Viewing the Allure Report

After the tests have been executed, you can generate and view the Allure report with:

```bash
allure serve allure-results
```

This command will open the Allure report in your default web browser.


---

## 📞 Contacts

Looking for an opportunity to start a career in test automation. Ready for test tasks, code reviews, and interviews.

- **GitHub:** [lobanov-qa](https://github.com/lobanov-qa)
- **LinkedIn:** [evgenii-lobanov-qa](https://www.linkedin.com/in/evgenii-lobanov-qa/)
- **Telegram:** [lobanov_e_i](https://t.me/lobanov_e_i)

---

*Project created as part of the ["API Test Automation with Python" course](https://stepik.org/course/233196/info) (author — Nikita Filonov).*
