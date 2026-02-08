from contextlib import asynccontextmanager
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import Settings
from routes import base, data

# 1. Define the lifespan logic
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Setup the database connection
    settings = Settings()
    app.mongodb_connect = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongodb_connect[settings.MONGODB_DATABASE]
    
    yield  # The app is now running and handling requests
    
    # Shutdown: Clean up the connection
    app.mongodb_connect.close()

# 2. Pass the lifespan to the FastAPI instance
app = FastAPI(lifespan=lifespan)

# Include your routes as usual
app.include_router(base.base_router)
app.include_router(data.data_router)