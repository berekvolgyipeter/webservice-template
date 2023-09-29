from flask import request
from functools import wraps


def get_params(func):
    @wraps(func)
    def run(*args, **kwargs):
        if request.method in ['POST', 'PUT', 'PATCH']:
            params = request.json
        else:
            params = dict(request.args)
        return func(params, *args, **kwargs)

    return run
