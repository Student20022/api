from flask_restful import Resource
from flask import request, jsonify, Blueprint
import simplexml

from app.db.session import get_session
from app.db.models.models import Statistics, Abbreviation

router = Blueprint("api_routers", __name__)


def format_arg(func):
    if request.args.get('format') == 'json':
        return jsonify(func)
    elif request.args.get('format') == 'xml':
        return simplexml.dumps({'report': func})


class ReportResource(Resource):
    def get(self):
        report_data = (
            get_session()
            .query(Statistics)
            .order_by(Statistics.position)
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
        
        return format_arg(serialized_data)


class DriverResource(Resource):
    def get(self):
        drivers = (
            get_session()
            .query(Abbreviation)
            .order_by(Abbreviation.id)
        )

        serialized_data = [
            {
                "Abbreviation": info.abbreviations,
                "Name": info.names,
                "Team": info.teams,
            }
            for info in drivers
        ]
        
        return format_arg(serialized_data)


class AboutResource(Resource):
    def get(self):
        driver_id = request.args.get('driver_id')

        driver = (
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
            for info in driver
        ]
        return format_arg(serialized_data)
