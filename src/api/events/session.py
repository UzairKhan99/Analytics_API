from sqlmodel import Field, Session, SQLModel, create_engine
from api.db.config import DATABASE_URL

if not DATABASE_URL:
    raise NotImplementedError("DATABASE URL needs to be set.")

engine = create_engine(DATABASE_URL)


def init_db():
    print("creating database")
    SQLModel.metadata.create_all(engine)
