from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy import text

from app.routes import data
from app.db import get_db, shutdown
import logging

logger = logging.getLogger('uvicorn.error')

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Setting up connection pool")
    get_db_context = asynccontextmanager(get_db)
    async with get_db_context() as db:
        await db.execute(text("SELECT 1"))
        yield
    
    logger.info("Stopping connection pool")
    await shutdown()

app = FastAPI(lifespan=lifespan)
app.include_router(data.router)
