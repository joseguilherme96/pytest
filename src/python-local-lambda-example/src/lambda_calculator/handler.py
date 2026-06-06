from enum import Enum
from pydantic import BaseModel,ValidationError
import json
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Action(Enum):

    plus = "plus"
    minus = "minus"
    times = "times"
    divided_by = "divided-by"

class HTTPStatus(Enum):

    SUCESS = 200
    REDIRECT = 302
    BAD_REQUEST = 400
    UN_AUTHORIZED = 401
    NOT_FOUND = 404
    CONFLICT = 409
    ERROR = 500

class InputEvent(BaseModel):
    class Config:
        use_enum_values = True

    action: Action
    x: int
    y: int

ACTIONS = {

    "plus": lambda x, y : x + y,
    "minus": lambda x, y : x - y,
    "times": lambda x, y : x * y,
    "divided-by": lambda x, y : x / y
}

def lambda_handler(event,context):

    logger.setLevel(os.environ.get("LOG_LEVEL", logging.INFO))
    logger.debug(f"Event: {event}")
    logger.debug(f"Context: {context}")
    response = None

    try:

        input_event = InputEvent(**event)
        action = input_event.action
        func = ACTIONS.get(input_event.action)
        x = input_event.x
        y = input_event.y
        status_code = 200

        try:

            if func is not None and \
                x is not None and \
                y is not None :

                result = func(x,y)
                response = f"{x} {action} {y} = {result}"
                logger.info(response)
                status_code = HTTPStatus.SUCESS.value

        except ZeroDivisionError:

            logger.warning(f"I can't divide {x} by 0!")
            response = f"I can't divide {x} by 0!"

    except ValidationError as e:

        status_code = HTTPStatus.BAD_REQUEST.value
        logger.error(e.errors())
        response = json.loads(e.json())

    except Exception as general_exception:

        status_code = HTTPStatus.ERROR.value
        logger.error(general_exception)
        response = "Internal Server Error Occured"

    return {
        "status_code": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Response ": response
        })
    }