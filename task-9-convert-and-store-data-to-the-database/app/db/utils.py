import logging

from sqlalchemy import text, create_engine
from sqlalchemy.exc import ProgrammingError

from app.config import settings
from app.logic.report.report import Report, read_file
from app.logic.report.config import ABBREVIATIONS
from app.db.session import get_session, engine
from app.db.models.models import (
    Statistics, 
    Abbreviation, 
    EndLog, 
    StartLog
)

log = logging.getLogger(__name__)


def create_database(db_name: str) -> None:
    try:
        with create_engine(
            settings.DATABASE_URL, isolation_level="AUTOCOMMIT"
        ).begin() as conn:
            conn.execute(text(f"CREATE DATABASE {db_name};"))
    except ProgrammingError:
        log.error("Database %s already exists", db_name)
    else:
        log.info("Database %s created", db_name)


def drop_database(db_name: str) -> None:
    try:
        with create_engine(
            settings.DATABASE_URL, isolation_level='AUTOCOMMIT'
        ).begin() as conn:
            conn.execute(text(f"DROP DATABASE {db_name} WITH (FORCE);"))
    except ProgrammingError:
        log.error("Database %s does not exist", db_name)
    else:
        log.info("Database %s dropped", db_name)


def init_db(db_url: str, db_name: str) -> None:
    import alembic.config
    import alembic.command

    alembic_config = alembic.config.Config("alembic.ini")
    alembic_config.set_main_option("sqlalchemy.url", f"{db_url}")
    alembic.command.upgrade(alembic_config, "head")
    log.info(f"alembic upgrade db: {db_url}")


def load_data_to_db(instance: Report, folder_path: str) -> None:
    Statistics.metadata.create_all(bind=engine)
    Abbreviation.metadata.create_all(bind=engine)
    StartLog.metadata.create_all(bind=engine)
    EndLog.metadata.create_all(bind=engine)
    
    with get_session() as conn:
        for driver, data in instance.sort_report().items():
            statistics_instance = Statistics(
                abbr=data.get("Abbreviation"),
                driver=data.get("Driver"),
                team=data.get("Team"),
                result=data.get("Result"),
                start=data.get("Start"),
                end=data.get("End"),
                position=data.get("Position"),
            )
            conn.add(statistics_instance)

        abbreviations = [
            i.split("_") for i in read_file(f"{folder_path}/{ABBREVIATIONS}")
        ]

        for i in abbreviations:
            abbreviation_instance = Abbreviation(
                abbreviations=i[0], 
                names=i[1], 
                teams=i[2]
            )
            conn.add(abbreviation_instance)

        for end, start in zip(instance.dict_end.items(), instance.dict_start.items()):
            end_log_instance = EndLog(
                abbreviations=end[0],
                dates=end[1].strftime("%Y-%m-%d"),
                times=end[1].strftime("%H:%M:%S"),
            )
            start_log_instance = StartLog(
                abbreviations=start[0],
                dates=start[1].strftime("%Y-%m-%d"),
                times=start[1].strftime("%H:%M:%S"),
            )
            conn.add(end_log_instance)
            conn.add(start_log_instance)
        conn.commit()
