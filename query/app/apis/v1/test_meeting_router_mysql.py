import httpx
from starlette.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_CONTENT,
)
from tortoise.contrib.test import TestCase

from query.app import app
from query.app.dtos.update_meeting_request import MEETING_DATE_MAX_RANGE
from query.app.tortoise_models.meeting import MeetingModel


class TestMeetingRouter(TestCase):
    async def test_api_create_meeting_mysql(self) -> None:
        # When
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app),
            base_url="http://test",
        ) as client:
            response = await client.post(url="/v1/mysql/meetings")

        # Then: 테스트 결과를 검증
        assert response.status_code == HTTP_200_OK
        url_code = response.json()["url_code"]
        assert (await MeetingModel.filter(url_code=url_code).exists()) is True

    async def test_can_not_update_meeting_date_range_when_range_is_too_long(
        self,
    ) -> None:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            # Given
            create_meeting_response = await client.post(url="/v1/mysql/meetings")
            url_code = create_meeting_response.json()["url_code"]

            # When
            response = await client.patch(
                url=f"/v1/mysql/meetings/{url_code}/date_range",
                json={
                    "start_date": (start := "2025-10-10"),
                    "end_date": (end := "2030-10-20"),
                },
            )

        # Then
        assert response.status_code == HTTP_422_UNPROCESSABLE_CONTENT
        response_body = response.json()
        assert (
            response_body["detail"]
            == f"start {start} and end {end} should be within {MEETING_DATE_MAX_RANGE.days} days"
        )

    async def test_can_not_update_meeting_date_range_when_it_is_already_set(
        self,
    ) -> None:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            # Given
            create_meeting_response = await client.post(url="/v1/mysql/meetings")
            url_code = create_meeting_response.json()["url_code"]
            await client.patch(
                url=f"/v1/mysql/meetings/{url_code}/date_range",
                json={"start_date": "2025-10-10", "end_date": "2025-10-20"},
            )

            # When
            response = await client.patch(
                url=f"/v1/mysql/meetings/{url_code}/date_range",
                json={"start_date": "2025-10-12", "end_date": "2025-10-22"},
            )

        # Then
        assert response.status_code == HTTP_422_UNPROCESSABLE_CONTENT
        response_body = response.json()
        assert (
            response_body["detail"]
            == f"meeting: {url_code} start: 2025-10-10 end: 2025-10-20 are already set"
        )

    async def test_can_not_update_meeting_does_not_exists(self) -> None:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            # Given
            url_code = "invalid_url"

            # When
            response = await client.patch(
                url=f"/v1/mysql/meetings/{url_code}/date_range",
                json={"start_date": "2025-10-12", "end_date": "2025-10-22"},
            )

        # Then
        assert response.status_code == HTTP_404_NOT_FOUND
        response_body = response.json()
        assert response_body["detail"] == "meeting with url_code: invalid_url not found"
