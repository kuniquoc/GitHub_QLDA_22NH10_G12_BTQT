from rest_framework.response import Response# type: ignore
from rest_framework import status# type: ignore
from .constants import ResponseMessage, EntityNames

class CustomResponse(Response):
    def __init__(self, data=None, message=None, status=None, **kwargs):
        response_data = {
            'code': status or 200,
            'message': message or 'Success',
            'data': data
        }
        super().__init__(data=response_data, status=status, **kwargs)

def create_response(status_code=status.HTTP_200_OK, message=None, data=None):
    if not message:
        message = "Success" if status_code < 400 else "Error"
        
    return Response(
        {
            "code": status_code,
            "message": message,
            "data": data
        },
        status=status_code
    )

def create_validation_error_response(errors):
    return create_response(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        message=ResponseMessage.VALIDATION_ERROR,
        data=errors
    )

def create_not_found_response(entity_name):
    return create_response(
        status_code=status.HTTP_404_NOT_FOUND,
        message=ResponseMessage.NOT_FOUND.format(entity_name)
    )

def create_success_response(data=None, message=None):
    return create_response(
        status_code=status.HTTP_200_OK,
        message=message or "Success",
        data=data
    )

def create_created_response(data=None, entity_name=None):
    message = ResponseMessage.CREATE_SUCCESS.format(entity_name) if entity_name else "Created successfully"
    return create_response(
        status_code=status.HTTP_201_CREATED,
        message=message,
        data=data
    )