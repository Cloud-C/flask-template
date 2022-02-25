from functools import wraps

from flask import request


def payload_checker(payload_field):
    def real_decorator(method, **kwargs):
        @wraps(method)
        def wrapper(*args, **kwargs):
            origin_payload = request.get_json(silent=True)
            new_payload = payload_field.validate(origin_payload)
            if not new_payload:
                raise Exception('payload can not be empty')

            return method(*args, **kwargs, payload=new_payload)

        return wrapper

    return real_decorator
