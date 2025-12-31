from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from test.meetifyr._app.apis.v1.meeting_router import (
    edgedb_router as meeting_edgedb_router,
)
from test.meetifyr._app.apis.v1.meeting_router import (
    mysql_router as meeting_mysql_router,
)

app = FastAPI(
    default_response_class=ORJSONResponse  # json 라이브러리 보다 빠른 성능이며 클라이언트에 ORJSON으로 변경해서 보낸다
)

app.include_router(meeting_edgedb_router)
app.include_router(meeting_mysql_router)
