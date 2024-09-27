from fastapi import FastAPI, HTTPException
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.config.db_config import mongodb,MONGO_URI,DATABASE_NAME
from app.config.logger_config import get_logger
from app.controller.users_controller import user_route
from app.controller.todos_controller import todos_route
from app.controller.project_controller import project_route


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/Project Management")
async def root():
    return {"message": "Welcome to Project Management"}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to MongoDB
    await mongodb.connect(MONGO_URI, DATABASE_NAME)
    yield

app.router.lifespan_context = lifespan
app.include_router(user_route, tags=["users"])
app.include_router(project_route,tags=["project"])
app.include_router(todos_route, tags=["todos"])