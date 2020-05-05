from http import HTTPStatus

from app.utilities.api_result import ApiResult


class ApiException(Exception):
    def __init__(self, payload, message, status=400):
        self.payload = payload
        self.message = message
        self.status = status

    def to_result(self):
        return ApiResult(
            payload=self.payload,
            message=self.message,
            status=self.status
        )


class UnAuthorized(ApiException):
    def __init__(
            self, payload={}, message=None, status=HTTPStatus.UNAUTHORIZED):
        if not message:
            message = 'Not authorized'
        super(UnAuthorized, self).__init__(payload, message, status)


class NotFound(ApiException):
    def __init__(self, payload={}, message=None, status=HTTPStatus.NOT_FOUND):
        if not message:
            message = 'Resource not found'
        super(NotFound, self).__init__(payload, message, status)
