from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"Data": "Server is running successfully"}

class Item(BaseModel):
    name: str
    brand: Optional[str] = None
    price: float

inventory = {  }



# Path parameters, in node we call it route params
# We can also have multiple path params like : @app.get("/get-item/{item_id}/{name}")
# @app.get("/get-item/{item_id}")
# def get_item(item_id: int):
#     print(item_id)
#     return inventory[item_id]

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(..., description="ID of the inventory that you want to fetch", gt=0)):  # where None is the default value
    print(item_id)
    return inventory[item_id]


# Query params : eg, ?queryparam=
# If u want to keep name as optional, we can write, def get_item_by_name(name: str = None): But fastapi documentation says, import Optional as well.
# With the * its considered as keyword args, and we added it because : name is optional. We cannot add optional args before required params.
@app.get("/get-by-name")
def get_item_by_name(*, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"data": "Item not found"}


# We can also combine path and query params like : 
@app.get("/get-by-name-combined/{item_id}")
def get_item_by_name_combined(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"data": "Item not found"}


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return "ID already exists"
    new_item = item
    inventory[item_id] = new_item

    return new_item