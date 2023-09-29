from flask import abort, make_response, jsonify


def http_exception(status_code: int, message: str):
    abort(make_response(jsonify({"message": message}), status_code))


class DriverNotFound(Exception):
    pass
