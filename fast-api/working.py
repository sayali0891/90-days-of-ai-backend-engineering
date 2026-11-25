from fastapi import FastAPI, Path, Query, HTTPException, status
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

class UpdateItem(BaseModel):
    name: Optional[str] = None
    brand: Optional[str] = None
    price: Optional[float] = None

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
    # return {"data": "Item not found"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found") 


# We can also combine path and query params like : 
@app.get("/get-by-name-combined/{item_id}")
def get_item_by_name_combined(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item not found")


# item here is the req.body param, its not a query or path param. 
# We implement req.body by impleting a class Item 
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        # return "ID already exists"
        raise HTTPException(status_code=404, detail="ID already exists")
    new_item = item
    inventory[item_id] = new_item

    return new_item


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        # return "ID does not exists"
        raise HTTPException(status_code=404, detail="ID does not exist")
    inventory[item_id] = item
    return inventory[item_id]


@app.patch("/update-item-patch/{item_id}")
def update_item_patch(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="ID does not exist")

    stored_item = inventory[item_id]

    # Extract ONLY the fields the client actually passed in the JSON request
    updated_value = item.model_dump(exclude_unset=True)

    # Create an updated copy of the existing Item model and save it back
    updated_item = stored_item.model_copy(update=updated_value)
    inventory[item_id] = updated_item

    return updated_item

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description= "Id to delete", gt=0)):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="ID does not exist")

    del inventory[item_id]
    return {"Success" : "Item deleted"}

"""
.model_dump() converts the incoming Pydantic object into a filtered dictionary of only changed fields, while .model_copy() merges that dictionary back into your existing Item object.
Because your inventory stores Pydantic Item models rather than plain Python dictionaries, you need both steps to bridge the gap between a Pydantic object and a dictionary.

1. Why we need .model_dump(exclude_unset=True)

When a client sends {"price": 500} to UpdateItem, Pydantic still sets the unprovided fields (name and brand) to their default value of None inside the object.
• Without exclude_unset=True: Dumping the model produces {"name": None, "brand": None, "price": 500}. Updating with this would accidentally wipe out your existing name and brand with None.
• With exclude_unset=True: Pydantic remembers which fields were actually sent in the JSON request and strips out everything else, giving you strictly {"price": 500}.

2. Why we need .model_copy(update=update_data)

In your /create-item endpoint, you saved a Pydantic Item object directly into inventory[item_id] (not a Python dict).
• A standard Python dict has .update(), but a Pydantic Item model does not.
• .model_copy(update=...) takes your existing stored_item (Item(name="Laptop", brand="Dell", price=800)), applies the {"price": 500} dictionary on top of it, and returns a brand-new, updated Item object (Item(name="Laptop", brand="Dell", price=500)) ready to be saved back to inventory.
"""

    
