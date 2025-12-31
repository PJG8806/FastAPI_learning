from fastapi import APIRouter

from test.meetifyr.app_meetifyr.dtos.create_meeting_response import CreateMeetingResponse

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["meeting"])
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["meeting"])
# 원래는 어떤 DB 를 쓰는지 RUL 에 적을 필요 없으며 실전에서는 DB 이름을 URL 에 넣으면 안된다


@edgedb_router.post("", description="meeting 을 생성합니다.")
async def api_create_meeting_edgedb() -> dict[str, str]:
    return {
        "url_code": "abc"
    }  # 이런 식으로 해도 되지만  필수 값인지 옵션인지 추가적인 필드가 있는지 모른다


# 직접 호출을 하지 않으면 어떤 key와 value가 들어있는지 모르며 실수로 key를 누락하거나 없는 key를 추가해도 오류를 잡기가 쉽지 않다
# dict는 froze 되어있지 않기 때문에 생성 이후 중간에 값이 바뀌어도 이를 알 수가 없습니다


@mysql_router.post("", description="meeting 을 생성합니다.")
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")  # 바뀌지 않는 abc 값을 전달한다


# 위에 데코레이션 붙은 함수를 path operation function이라고 불린다
