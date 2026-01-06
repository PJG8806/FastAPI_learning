import httpx
from httpx import AsyncClient
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from query.app import app
from query.app.utils.edge import edgedb_client


async def test_api_create_meeting_edgedb() -> None:
    # When
    async with AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.post(
            url="/v1/edgedb/meetings",
        )

    # Then
    assert response.status_code == HTTP_200_OK
    url_code = response.json()["url_code"]
    assert (
        await edgedb_client.query_single(
            f"select exists (select Meeting filter .url_code = '{url_code}');"
        )
        is True
    )


async def test_api_get_meeting() -> None:
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://test"
    ) as client:
        create_meeting_response = await client.post(
            url="/v1/edgedb/meetings",
        )
        url_code = create_meeting_response.json()["url_code"]

        response = await client.get(url=f"/v1/edgedb/meetings/{url_code}")

    assert response.status_code == HTTP_200_OK
    response_body = response.json()
    assert response_body["url_code"] == url_code


async def test_api_get_meeting_404() -> None:
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get(url="/v1/edgedb/meetings/invalid_url}")

    assert response.status_code == HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "meeting with url_code: invalid_url not found"
