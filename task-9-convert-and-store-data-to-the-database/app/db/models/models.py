from sqlalchemy import String, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models.base import Base
from app.db.session import engine


class Statistics(Base):
    __tablename__ = "Statistics"

    id: Mapped[int] = mapped_column(primary_key=True)
    abbr: Mapped[str] = mapped_column(String)
    driver: Mapped[str] = mapped_column(String, unique=True)
    team: Mapped[str] = mapped_column(String)
    result: Mapped[float] = mapped_column(Float)
    start: Mapped[str] = mapped_column(String)
    end: Mapped[str] = mapped_column(String)
    position: Mapped[int] = mapped_column(Integer)


class Abbreviation(Base):
    __tablename__ = "Abbreviation"

    id: Mapped[int] = mapped_column(primary_key=True)
    abbreviations: Mapped[str] = mapped_column(String, unique=True)
    names: Mapped[str] = mapped_column(String)
    teams: Mapped[str] = mapped_column(String)


class EndLog(Base):
    __tablename__ = "EndLog"

    id: Mapped[int] = mapped_column(primary_key=True)
    abbreviations: Mapped[str] = mapped_column(String, unique=True)
    dates: Mapped[str] = mapped_column(String)
    times: Mapped[str] = mapped_column(String)


class StartLog(Base):
    __tablename__ = "StartLog"

    id: Mapped[int] = mapped_column(primary_key=True)
    abbreviations: Mapped[str] = mapped_column(String, unique=True)
    dates: Mapped[str] = mapped_column(String)
    times: Mapped[str] = mapped_column(String)
    