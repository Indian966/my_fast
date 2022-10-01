from fastapi import FastAPI

app = FastAPI()

#   RGB2DMC
#   RGB 코드로 가장 유사한 십자수 실을 찾아준다.


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
