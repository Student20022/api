import pytest

from app.app import create_app
from app.config import settings
from app.db.session import get_session
from app.logic.report.report import Report
from app.db.utils import (
    create_database, 
    drop_database, 
    init_db, 
    load_data_to_db
)


@pytest.fixture(scope="session")
def client():
    create_app().config["TESTING"] = True
    with create_app().test_client() as client:
        yield client


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    report = Report(folder_path="data")
    create_database(db_name=settings.DB_NAME)
    load_data_to_db(instance=report, folder_path="data")
    init_db(settings.DATABASE_URL_psycopg, settings.DB_NAME)


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    try:
        get_session().close()
    finally:
        print("\nDB closed")
    try:
        drop_database(settings.DB_NAME)
    finally:
        print("Database dropped")
