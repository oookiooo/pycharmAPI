from fastapi import FastAPI
import Models.ItemModel as ItemModel
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
@app.post("/items/")
async def create_item():
    item = ItemModel.Item("arek","arek",13.1,23.1)
    print("sads")
    return item
