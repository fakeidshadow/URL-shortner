from fastapi import FastAPI
from app.controllers.link_controller import router as link_router

app = FastAPI()
app.include_router(link_router)
