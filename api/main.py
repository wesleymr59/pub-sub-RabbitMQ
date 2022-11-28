from fastapi import FastAPI
from routers import mainRouters
import uvicorn

app = FastAPI()

app.include_router(mainRouters.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")