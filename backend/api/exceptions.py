import logging
from rest_framework.views import exception_handler
from rest_framework.exceptions import (
    Throttled,
    AuthenticationFailed,
    NotAuthenticated,
    MethodNotAllowed,
    ParseError,
    PermissionDenied,
)
from rest_framework.response import Response  # noqa

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, Throttled):
        custom_response_data = {"message": exc.detail}
        response.data = custom_response_data

    elif isinstance(exc, AuthenticationFailed) or isinstance(exc, NotAuthenticated):
        custom_response_data = {"message": exc.detail}
        response.data = custom_response_data

    elif isinstance(exc, MethodNotAllowed):
        custom_response_data = {"message": exc.detail}
        response.data = custom_response_data

    elif isinstance(exc, ParseError):
        custom_response_data = {"message": exc.detail}
        response.data = custom_response_data

    elif isinstance(exc, PermissionDenied):
        custom_response_data = {
            "message": "You do not have permission to access this resource"
        }
        response.data = custom_response_data

    # elif isinstance(exc, Exception) and getattr(exc, "status_code", None) is None:
    #     logger.exception(exc)
    #     response = Response(
    #         {"message": "Internal Server Error", "trace": str(exc)}, status=500
    #     )
    # return response
