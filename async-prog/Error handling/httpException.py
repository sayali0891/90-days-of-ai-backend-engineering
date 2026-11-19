from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import uvicorn

from customExceptionHandler import ItemNotFoundError

app = FastAPI()

items = {"1": "Laptop", "2": "Smartphone"}

@app.exception_handler(ItemNotFoundError)
async def item_not_found_custom_handler(request: Request, exc: ItemNotFoundError):
    return JSONResponse(
        status_code = 404,
        content = {
            "message": exc.message,
            "item_id" : exc.item_id
        }
    )

@app.get("/items/{item_id}")
async def get_item(item_id : str):
    if item_id not in items:          
    #HttpException
        #raise HTTPException(404, detail={"error_code" : "Item not found", "message": f"Item {item_id} does not exist."})

    # Custom Exception Handler : 
        raise ItemNotFoundError(item_id=item_id)


    
    return {"message" : "Item found", "item": items[item_id]}


if __name__ == "__main__":
    uvicorn.run("httpException:app", reload=True)

