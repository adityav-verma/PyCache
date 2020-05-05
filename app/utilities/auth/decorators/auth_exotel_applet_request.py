"""Decorator to validate requests from Exotel Applet Webhooks"""
from flask import request, current_app
from functools import wraps
from http import HTTPStatus

from app.exceptions import UnAuthorized


def authorize_exotel_applet_request(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        request_args = request.args or {}
        token = current_app.config.get(
            'EXOTEL', {}
        ).get('APPLET_REQUEST_TOKEN')
        if token != request_args.get('auth_token'):
            raise UnAuthorized(
                {}, 'Invalid auth_token', HTTPStatus.UNAUTHORIZED
            )
        return f(*args, **kwargs)
    return decorated_function
