from fastapi import FastAPI
from routers import mainRouters

app = FastAPI()

app.include_router(mainRouters.router)