from sqlmodel import Field, Session, SQLModel, create_engine
from api.db.config import DATABASE_URL
import timescaledb
if not DATABASE_URL:
    raise NotImplementedError("DATABASE URL needs to be set.")

engine = timescaledb.create_engine(DATABASE_URL, timezone='UTC')


def init_db():
    print("creating database")
    SQLModel.metadata.create_all(engine)
    print("creating hypertables")
    timescaledb.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
 