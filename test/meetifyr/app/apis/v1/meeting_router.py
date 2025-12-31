from fastapi import APIRouter

from test.meetifyr.app.dtos.create_meeting_response import CreateMeetingResponse

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["meeting"])
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["meeting"])
# 원래는 어떤 DB 를 쓰는지 RUL 에 적을 필요 없으며 실전에서는 DB 이름을 URL 에 넣으면 안된다


@edgedb_router.post("", description="meeting 을 생성합니다.")
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")  # 바뀌지 않는 abc 값을 전달한다


@mysql_router.post("", description="meeting 을 생성합니다.")
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")


# 위에 데코레이션 붙은 함수를 path operation function이라고 불린다
