from fastapi import FastAPI
import requests
app = FastAPI()

#   RGB2DMC
#   RGB 코드로 가장 유사한 십자수 실을 찾아준다.


@app.get("/rgb2dmc")
async def root():
    return {"message": "Hello World"}


@app.post("/rgb2dmc")
async def say_hello(r : int, g: int, b: int):
    rgb_code = (r, g, b)
    return {"message": f"Hello {rgb_code}"}
