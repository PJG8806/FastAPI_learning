set -eo pipefail

COLOR_GREEN=`tput setaf 2;` #성공하면 색상
COLOR_NC=`tput sgr0;` # 아니면 색상없음

echo "Starting black"
poetry run black test
echo "OK"

echo "Starting ruff"
poetry run ruff check --select I --fix # 임폹트 정렬 실행
poetry run ruff check --fix
echo "OK"

echo "Starting mypy"
poetry run mypy test
echo "OK"

ecoh "Starting pytest with coverage"
poetry run coverage run -m pytest
poetry run coverage report -m
poetry run coverage html
echo "OK"

echo "${COLOR_GREEN}All tests passed successfully!${COLOR_NC}"
