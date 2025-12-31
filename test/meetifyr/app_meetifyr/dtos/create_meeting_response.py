from typing import Annotated

from pydantic import BaseModel, Field

from test.meetifyr.app_meetifyr.dtos.frozen_config import FROZEN_CONFIG


class CreateMeetingResponse(BaseModel):
    model_config = FROZEN_CONFIG

    url_code: Annotated[str, Field(description="미팅 url 코드. unique 합니다.")]
    # Annotated 는 타입이 str이지만 라이브러리에 요구한 설정을 부차적으로 넣을수 있다
