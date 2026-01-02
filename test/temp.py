import string
from typing import (
    ClassVar,
)  # ClassVar 클래스 변수로 클래스 레벨에서 정의하고 사용하는 변수


class Base62:
    BASE: ClassVar[str] = string.ascii_letters + string.digits
    BASE_LEN: ClassVar[int] = len(BASE)

    @classmethod
    def encode(cls, num: int) -> str:
        if num < 0:
            raise ValueError(
                f"{cls}.encode() needs positive integer but you passed: {num}"
            )

        if num == 0:
            return cls.BASE[0]

        result = []
        while num:
            num, remainder = divmod(
                num, cls.BASE_LEN
            )  # divmod 한번 나누고 목과 나머지를 구한다
            result.append(cls.BASE[remainder])
        return "".join(
            result
        )  # join 문자를 합치면서 "".에 값을 넣으면 사이사이에 넣은 값이 들어간다


print(Base62.encode(94))
