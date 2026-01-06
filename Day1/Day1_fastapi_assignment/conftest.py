# conftest.py

import pytest
from Day1.Day1_fastapi_assignment.app.models.users import UserModel

TEST_BASE_URL = "http://test"


@pytest.fixture(scope="function", autouse=True)
def user_model_clear() -> None:
    UserModel.clear()
