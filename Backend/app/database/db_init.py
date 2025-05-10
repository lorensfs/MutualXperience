from sqlmodel import SQLModel, Session, create_engine
from app.core.config import settings

database_uri = str(settings.SQLMODEL_DATABASE_URI)
engine = create_engine(database_uri, echo=True)

def setup_database():
    SQLModel.metadata.create_all(bind=engine)

def get_db():
    with Session(engine) as session:
        yield session
