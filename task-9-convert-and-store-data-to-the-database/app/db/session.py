import logging

from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine

from app.config import settings, ENGINE_OPTIONS


log = logging.getLogger(__name__)

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    **ENGINE_OPTIONS,
    pool_size=10,
    max_overflow=10,
)


def get_session() -> Session:
    session = sessionmaker(engine)
    return session()
