

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/attendance")
async def root():
    return {"message": "Welcome to attendance"}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to MongoDB
    await mongodb.connect(MONGO_URI, DATABASE_NAME)
    yield

app.router.lifespan_context = lifespan
app.include_router(user_route, tags=["users"])