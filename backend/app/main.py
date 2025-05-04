from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/test")
async def test():
    return {"message": "api_test"}

@app.get("/api/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}