from fastapi import FastAPI
import requests
app = FastAPI()

#   App Name : RGB2DMC
#   Description : RGB 코드로 가장 유사한 십자수 실을 찾아 준다.
#   Input data : RGB code ex) (255,255,255)
#   Output data : Floss, Description, RGB Code(Hexadecimal),(Picture of Color)


@app.get("/rgb2dmc")
async def root():
    return {"message": "Hello World"}


@app.post("/rgb2dmc")
async def say_hello(r : int, g: int, b: int):
    rgb_code = (r, g, b)
    return {"message": f"Hello {rgb_code}"}
