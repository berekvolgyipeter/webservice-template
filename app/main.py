from app.constants import IS_DEV_ENVIRONMENT, APP_HOST, APP_PORT
from app.global_objects import app
from app.routes.drivers import api as drivers_api
from app.routes.health import api as health_api
from app.routes.results import api as results_api


app.register_blueprint(drivers_api)
app.register_blueprint(health_api)
app.register_blueprint(results_api)


if __name__ == "__main__":
    app.run(debug=IS_DEV_ENVIRONMENT, host=APP_HOST, port=APP_PORT)
