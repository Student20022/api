from flask import Flask
from flask_restful import Api

from app.routers.app_routers import router as app_router
from app.routers.api_routers import router as api_router
from app.routers.api_routers import (
    DriverResource,
    ReportResource,
    AboutResource,
)


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.register_blueprint(app_router)
    app.register_blueprint(api_router)

    api.add_resource(ReportResource, '/api/v1/report/')
    api.add_resource(DriverResource, '/api/v1/report/drivers/')
    api.add_resource(AboutResource, '/api/v1/report/drivers/about/')

    return app


if __name__ == '__main__':
    create_app().run(debug=True)