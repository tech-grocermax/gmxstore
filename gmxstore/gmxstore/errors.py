"""
error.py

Exception definitions and a helper function.
Use 'register_errorhandlers' to enable exception handling.
"""
from flask import make_response
from requests import codes
import ujson


class BadInputValue(Exception):
    code = codes.BAD_REQUEST

    def __init__(self, key):
        message = "Invalid value for key: '{}'".format(key)
        super(BadInputValue, self).__init__(message)


class DuplicateReceipt(Exception):
    code = codes.CONFLICT

    def __init__(self):
        message = "This receipt has already been stored"
        super(DuplicateReceipt, self).__init__(message)


class DuplicateTransactionId(Exception):
    code = codes.CONFLICT

    def __init__(self):
        message = "This receipt has duplicate transaction id."
        super(DuplicateTransactionId, self).__init__(message)


class NoRecordFound(Exception):
    code = codes.NOT_FOUND

    def __init__(self, message="No record found."):
        super(NoRecordFound, self).__init__(message)


class InvalidReceiptUpdateRequest(Exception):
    code = codes.CONFLICT

    def __init__(self):
        message = "Updating existing receipt with PENDING status not allowed."
        super(InvalidReceiptUpdateRequest, self).__init__(message)


class UnauthorizedUserError(Exception):
    code = codes.UNAUTHORIZED

    def __init__(self):
        message = 'Authentication credentials either invalid or not provided'
        super(UnauthorizedUserError, self).__init__(message)


class BadInputParam(Exception):
    code = codes.BAD_REQUEST

    def __init__(self, key):
        message = "'{}' is extra or missing".format(key)
        super(BadInputParam, self).__init__(message)


def register_errorhandlers(app):
    @app.errorhandler(BadInputParam)
    def bad_param(error):
        return _create_error_response(error.code, error.message)

    @app.errorhandler(BadInputValue)
    def bad_value(error):
        return _create_error_response(error.code, error.message)

    @app.errorhandler(BadInputParam)
    def bad_input(error):
        return _create_error_response(error.code, error.message)

    @app.errorhandler(DuplicateReceipt)
    def duplicate_receipt(error):
        return _create_error_response(error.code, error.message)

    @app.errorhandler(UnauthorizedUserError)
    def bad_auth_user(error):
        return _create_error_response(error.code, error.message)

    @app.errorhandler(codes.NOT_FOUND)
    def not_found(error):
        return _create_error_response(error.code, error.description)

    @app.errorhandler(codes.UNAUTHORIZED)
    def bad_auth(error):
        return _create_error_response(error.code, error.description)

    @app.errorhandler(codes.UNSUPPORTED_MEDIA_TYPE)
    def bad_media_type(error):
        return _create_error_response(error.code, error.description)

    @app.errorhandler(codes.CONFLICT)
    def conflict(error):
        return _create_error_response(error.code, error.description)

    @app.errorhandler(InvalidReceiptUpdateRequest)
    def invalid_receipt_update_request(error):
        return _create_error_response(error.code, error.message)

    @app.errorhandler(DuplicateTransactionId)
    def duplicate_transaction_id(error):
        return _create_error_response(error.code, error.message)

    @app.errorhandler(NoRecordFound)
    def no_record_found(error):
        return _create_error_response(error.code, error.message)


def _create_error_response(code, message):
    response_body = {"error_message": message, "error_code": code}
    response = make_response(ujson.dumps(response_body))
    response.status_code = code
    response.error_message = message
    return response
