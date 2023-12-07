from enum import Enum
from typing import Optional

from pydantic import BaseModel
from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.get("/")
async def root():
    """
    Example: http://127.0.0.1:8000
    """
    return {"message": "Hello World"}


@app.get("/users")
async def read_users2():
    """
    This is description
    http://127.0.0.1:8000/users
    """
    return ["Bean", "Elfo"]


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    """
    This is description
    http://127.0.0.1:8000/users/1
    """
    return {"user_id": user_id}


@app.get("/users/me")
async def read_user_me():
    """
    This is description
    http://127.0.0.1:8000/users/me
    """
    return {"user_id": "the current user"}


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    """
    Multiple path and query parameter
    http://127.0.0.1:8000/users/1/items/2?short=True
    """
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )

    if short:
        item.update({"short": short})

    return item


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """
    Get model from a model name
    http://127.0.0.1:8000/models/alexnet
    """
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Example: http://127.0.0.1:8000/items/1
    """
    return {"item_id": item_id}


@app.get("/items/")
async def read_items():
    """
    Example: http://127.0.0.1:8000/items
    """
    items = [Item(name="Mercedes C300", description="Luxury", price=50000, tax=500),
             Item(name="Mercedes C200", description="Normal", price=40000, tax=400)]
    return items


@app.post("/items/")
async def create_item(item: Item):
    return item

