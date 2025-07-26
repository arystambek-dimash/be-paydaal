from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


def create_engine(db_url: str) -> AsyncEngine:
    return create_async_engine(db_url)


def create_db_session(engine: AsyncEngine) -> async_sessionmaker:
    session = async_sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False,
        autocommit=False
    )
    return session


class Base(DeclarativeBase):
    ...
