from contextlib import asynccontextmanager
from decimal import getcontext

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.main import api_router
from app.core.config import settings
from app.database.db_init import setup_database
# from app.database.initial_data.init_db import init_db
from app.database.session import SessionLocal
from app.logger import get_logger

getcontext().prec = 18

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app_instance: FastAPI):
    session = SessionLocal()
    setup_database()
    try:
        logger.info("Initializing database.")
        # init_db(session)
        # scheduler here
        # scheduler.start()
        # load_tasks(session)
        yield
    finally:
        logger.info("Shutting down.")
        # close scheduler here
        # scheduler.shutdown()
        session.close()


app = FastAPI(
    lifespan=lifespan,
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)


@app.get("/")
async def root():
    return {
        "project_name": settings.PROJECT_NAME,
    }


@app.get("/health")
async def health():
    return {"status": "OK"}


if settings.all_cors_origins:
    # noinspection PyTypeChecker
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
