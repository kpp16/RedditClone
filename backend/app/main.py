from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .repositories.database import engine, Base
from .config import config
from .routers import postRouter, commentsRouter

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(postRouter.router)
app.include_router(commentsRouter.router)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/info")
async def info():
    return {
        "app_name": config.ApplicatonSettings.APP_NAME,
    }

    
@app.get("/")
def root():
    return {"message": "Hello, World"}
