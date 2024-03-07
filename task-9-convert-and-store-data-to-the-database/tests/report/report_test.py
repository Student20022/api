import pytest
import datetime

from app.logic.report.report import (
    Report, 
    validator_not_exist_files
)


invalid_folder = "/path/to/nonexistent/folder"
folder_path = "data"

test_abbr = (
    ("DRR", "Daniel Ricciardo_RED BULL RACING TAG HEUER"),
    ("SVF", "Sebastian Vettel_FERRARI"),
    ("LHM", "Lewis Hamilton_MERCEDES"),
)

test_time_calculate = {
    "MES": datetime.timedelta(seconds=73, microseconds=265000).total_seconds(),
    "RGH": datetime.timedelta(seconds=72, microseconds=930000).total_seconds(),
    "SPF": datetime.timedelta(seconds=72, microseconds=848000).total_seconds(),
    "LSW": datetime.timedelta(seconds=73, microseconds=323000).total_seconds(),
    "DRR": datetime.timedelta(seconds=167, microseconds=987000).total_seconds(),
    "NHR": datetime.timedelta(seconds=73, microseconds=65000).total_seconds(),
    "CSR": datetime.timedelta(seconds=72, microseconds=950000).total_seconds(),
    "KMH": datetime.timedelta(seconds=73, microseconds=393000).total_seconds(),
    "BHS": datetime.timedelta(seconds=73, microseconds=179000).total_seconds(),
    "SVM": datetime.timedelta(seconds=72, microseconds=463000).total_seconds(),
    "KRF": datetime.timedelta(seconds=72, microseconds=639000).total_seconds(),
    "VBM": datetime.timedelta(seconds=72, microseconds=434000).total_seconds(),
    "SVF": datetime.timedelta(seconds=64, microseconds=415000).total_seconds(),
    "EOF": datetime.timedelta(seconds=346, microseconds=972000).total_seconds(),
    "PGS": datetime.timedelta(seconds=72, microseconds=941000).total_seconds(),
    "SSW": datetime.timedelta(seconds=287, microseconds=294000).total_seconds(),
    "FAM": datetime.timedelta(seconds=72, microseconds=657000).total_seconds(),
    "CLS": datetime.timedelta(seconds=72, microseconds=829000).total_seconds(),
    "LHM": datetime.timedelta(seconds=407, microseconds=540000).total_seconds(),
}

test_driver_info_data = {
    "Driver": "Sebastian Vettel",
    "Position": 1,
}


def test_validator_valid_folder() -> None:
    assert validator_not_exist_files(folder_path) == set()


def test_validator_invalid_folder():
    with pytest.raises(FileNotFoundError):
        validator_not_exist_files(folder_path=invalid_folder)


@pytest.mark.parametrize("abbr, driver_info", test_abbr)
def test_get_abbreviations(abbr, driver_info) -> None:
    report = Report(folder_path)
    abbr_data = report.get_abbreviations()
    assert len(abbr_data) == 19
    assert abbr_data[abbr] == driver_info


def test_time_calculator() -> None:
    report = Report(folder_path)
    data = report.time_calculator()

    for key, value in data:
        assert test_time_calculate[key] == value


def test_driver_info() -> None:
    report = Report(folder_path, driver="SVF")
    data = report.sort_report().get("SVF")
    assert data
    assert data['Driver'] == test_driver_info_data["Driver"]
    assert data['Position'] == test_driver_info_data["Position"]

