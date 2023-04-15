import re
import json

from flask import request, abort
from functools import wraps


# matches 2020-01-23
def validate_date_format(date):
    if date:
        pattern = re.compile(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$")
        if not bool(pattern.match(str(date))):
            abort(400, "Invalid date format. Format must match 'yyyy-mm-dd'")

# matches 2020-01-23 23:59:01
def validate_datetime_format(datetime):
    if datetime:
        pattern = re.compile(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01]) (0[0-9]|1[0-9]|2[0-3]):(0[0-9]|[1-5][0-9]):(0[0-9]|[0-5][0-9])(\.\d+)?$")
        if not bool(pattern.match(str(datetime))):
            abort(400, "Invalid datetime format. Format must match 'yyyy-mm-dd hh:mm:ss'")

def validate_fields(fields, data):
    # Split the fields string into a list of required and optional fields
    required_fields = []
    optional_fields = []

    for field in fields.split(' '):
        if field.startswith('['):
            optional_fields.append(field[1:-1])
        else:
            required_fields.append(field)

    # Ensure there are no additional fields
    for field in data:
        if field not in required_fields and field not in optional_fields:
            abort(400, 'Unexpected field: {}'.format(field))

    # Ensure all required fields are present
    for field in required_fields:
        if field not in data:
            abort(400, 'Missing field: {}'.format(field))


def requires_body(fields=''):
    def requires_body_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            body = {}

            if request.data:
                body = json.loads(request.data, strict=False)

            validate_fields(fields, body)

            return f(body, *args, **kwargs)

        return wrapper
    return requires_body_decorator
