import logging

from flask import Flask
from pydantic import ValidationError

from backend.database import db_session
from backend.disticts.views import district_view
from backend.sirens.views import siren_view
from backend.errors import AppError


app = Flask(__name__)
app.register_blueprint(district_view, url_prefix='/api/districts')
app.register_blueprint(siren_view, url_prefix='/api/sirens')


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def shutdown_session(exception=None):
    db_session.remove()


def handle_validation_error(err: ValidationError):
    return {'error': str(err)}, 400


def handle_app_error(err: AppError):
    return {'error': str(err)}, err.code


app.register_error_handler(AppError, handle_app_error)
app.register_error_handler(ValidationError, handle_validation_error)
app.teardown_appcontext(shutdown_session)


def main():
    logger.info('Started successfully')
    app.run(host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()
