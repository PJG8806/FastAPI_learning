# conftest.py

import pytest
from Day4.fastapi_assignment.app.models.users import UserModel

TEST_BASE_URL = "http://test"


@pytest.fixture(scope="function", autouse=True)
def user_model_clear() -> None:
    UserModel.clear()
