from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import time
# from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

# app.add_middleware(GZipMiddleware, minimum_size=1000)

# custom middleware : Writing a simple logger middleware to intercept incoming requests.
@app.middleware("http")
async def log_request(request: Request, call_next):
    # Record start time
    start_time = time.time()

    # Intercept and process the incoming request
    resp = await call_next(request)

    process_time = time.time() - start_time

    # Print or log the details
    print(f"Path: {request.url.path} | Method: {request.method} | Duration: {process_time:.4f}s | Status: {resp.status_code}")
    
    return resp

@app.get("/timepass")
def read_timepass():
    return {"message": "Hello World"}

@app.get("/")
def home():
    return {"message": "CORS enabled!"}

if __name__ == "__main__":
    uvicorn.run("middleware:app", reload=True)
