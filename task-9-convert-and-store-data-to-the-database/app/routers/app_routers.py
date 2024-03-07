from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
    Response,
    jsonify,
)

from app.db.models.models import Statistics, Abbreviation
from app.logic.report.report import Report
from app.db.session import get_session

from flask_restful import Api
from tabulate import tabulate


router = Blueprint("app_routers", __name__)


@router.route("/")
def index():
    return redirect("/report")


@router.route("/report")
@router.route("/report/")
def report_page() -> Response:
    request_order = request.args.get("order", "asc")

    report_data = (
        get_session()
        .query(Statistics)
        .order_by(Statistics.position)
        .all()
    )

    if request_order == "desc":
        report_data = (
            get_session()
            .query(Statistics)
            .order_by(Statistics.position.desc())
            .all()
        )

    serialized_data = [
        {
            "Position": stat.position,
            "Abbreviation": stat.abbr,
            "Driver": stat.driver,
            "Team": stat.team,
            "Result": stat.result,
            "Start": stat.start,
            "End": stat.end,
        }
        for stat in report_data
    ]

    return Response(
        tabulate(serialized_data, headers="keys", tablefmt="jira"),
        content_type="text/plain; charset=utf-8",
    )


@router.route("/report/drivers/")
def driver_list() -> str:
    request_order = request.args.get("order", "asc")

    drivers = (
        get_session()
        .query(Abbreviation)
        .order_by(Abbreviation.abbreviations)
        .all()
    )

    if request_order == "desc":
        drivers = (
            get_session()
            .query(Abbreviation)
            .order_by(Abbreviation.abbreviations.desc())
            .all()
        )

    serialized_data = [
        {
            "Abbreviation": info.abbreviations,
            "Name": info.names,
            "Team": info.teams,
        }
        for info in drivers
    ]

    return render_template("drivers.html", info=serialized_data)


@router.route("/report/drivers")
def about_driver():
    driver_id = request.args.get("driver_id")

    report_data = (
        get_session()
        .query(Statistics)
        .filter_by(abbr=driver_id)
        .all()
    )

    serialized_data = [
        {
            "Position": info.position,
            "Abbreviation": info.abbr,
            "Driver": info.driver,
            "Team": info.team,
            "Result": info.result,
            "Start": info.start,
            "End": info.end,
        }
        for info in report_data
    ]

    return jsonify(serialized_data)
