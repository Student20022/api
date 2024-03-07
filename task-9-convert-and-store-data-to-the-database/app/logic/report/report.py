from typing import Any, Optional, Literal
from datetime import datetime
import os

from app.logic.report.config import (
    ABBREVIATIONS,
    END_LOG,
    START_LOG,
    TIME_FMT,
    TOP_LIST_LIMIT
)


def read_file(folder_path: str) -> list[str]:
    with open(folder_path, "r") as fp:
        return [line.strip() for line in fp.read().splitlines() if line]


def validator_not_exist_files(folder_path: str) -> set[str]:
    return {ABBREVIATIONS, END_LOG, START_LOG} - set(os.listdir(folder_path))


class Report:
    def __init__(
        self,
        folder_path: str,
        order_by: Literal["asc", "desc"] = "asc",
        driver: Optional[str] = None,
    ) -> None:
        self.folder_path = folder_path
        self.order_by = order_by
        self.reverse = order_by == "desc"
        self.driver = driver

        self.dict_end = self.parser_log(END_LOG)
        self.dict_start = self.parser_log(START_LOG)

    def parser_log(self, file_name: str) -> dict[str, datetime]:
        return {
            line[:3]: datetime.strptime(line[3:], TIME_FMT)
            for line in read_file(self.folder_path + "/" + file_name)
        }

    def get_abbreviations(self) -> dict[str, str]:
        return {
            text[:3]: text[4:]
            for text in read_file(self.folder_path + "/" + ABBREVIATIONS)
        }

    def time_calculator(self) -> tuple[tuple[str, float], ...]:
        dictionary = {}

        for key, end_time in self.dict_end.items():
            if (start_time := self.dict_start.get(key)) is not None:
                if (difference := end_time - start_time).total_seconds() > 0:
                    dictionary[key] = difference.total_seconds()
                else:
                    dictionary[key] = abs(difference).total_seconds()

        return tuple(sorted(dictionary.items(), key=lambda item: item[1]))

    def sort_report(self) -> dict[str, dict[str, Any]]:
        result = {}
        abbr_data = self.get_abbreviations()
        times_data = self.time_calculator()

        for pos, (key, value) in enumerate(times_data, start=1):
            driver, team = abbr_data[key].split("_")
            driver_info = {}
            driver_info["Abbreviation"] = key
            driver_info["Driver"] = driver
            driver_info["Team"] = team
            driver_info["Result"] = value
            driver_info["Start"] = self.dict_start[key]
            driver_info["End"] = self.dict_end[key]
            driver_info["Position"] = pos
            result[key] = driver_info

        return result

    def print_driver_info(self, result: dict[str, Any]) -> None:
        print(f"Driver: {result['Driver']}", end=" ")
        print(f"Team: {result['Team']}", end=" ")
        print(f"Result: {result['Result']}", end=" ")
        print(f"Start: {result['Start']}", end=" ")
        print(f"End: {result['End']}", end=" ")
        print(f"Position: {result['Position']}")

    def print_report(self) -> None:
        report = self.sort_report()
        print("------Printing report------")
        if self.driver is not None:
            result = report.get(self.driver)
            if result is None:
                print(f"Driver {self.driver} not found")
            else:
                self.print_driver_info(result)
        else:
            report_data = tuple(report.values())
            if self.reverse:
                report_data = reversed(report_data)
            for driver_info in report_data:
                if driver_info["Position"] == TOP_LIST_LIMIT:
                    print("---------------------------")
                self.print_driver_info(driver_info)
