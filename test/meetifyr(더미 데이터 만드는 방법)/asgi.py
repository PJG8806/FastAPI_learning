from meetifyr_app import app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

"""
정리
 구현 보다 앞서 스펙을 확정하고 스펙 + 더미 response 먼저 만들어 배포하자
 timeit를 사용해서 간단한 파이썬 코드조각을 성능테스트 할 수 있다
 pydantic 으로 dto를 생성할 수 있다
 dict 대신 dto를 사용하자
 dto는 data 전달하기 위한 목적으로 생성한 객체이고 수정, 추가, 삭제를 추가하면 dto가 아니게 된다
"""
