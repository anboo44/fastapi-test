from fastapi import FastAPI

app = FastAPI(title = "FastAPI-School")

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/say-hello")
async def say_hello():
    return {"message": "Ok"}
