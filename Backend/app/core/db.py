from sqlmodel import SQLModel, create_engine, Session
from typing import Generator
import psycopg
from app.core.config import settings

DATABASE_URL = f"postgresql+psycopg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

engine = create_engine(DATABASE_URL, echo=True)

def get_engine():
    return engine

def create_database_if_not_exists():
    try:
        # Connect to the default database using psycopg (psycopg3)
        with psycopg.connect(
            dbname="postgres",
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
            autocommit=True
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT 1 FROM pg_database WHERE datname = %s", (settings.POSTGRES_DB,))
                exists = cur.fetchone()
                if not exists:
                    cur.execute(f"CREATE DATABASE {settings.POSTGRES_DB}")
                    print(f"Database {settings.POSTGRES_DB} created.")
    except Exception as e:
        print(f"Error while checking or creating the database: {e}")
        raise

def init_db():
    create_database_if_not_exists()
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator:
    with Session(engine) as session:
        yield session
