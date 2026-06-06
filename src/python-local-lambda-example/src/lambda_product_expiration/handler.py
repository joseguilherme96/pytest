import json
from enum import Enum
from pydantic import BaseModel
import logging
from datetime import datetime
from datetime import timedelta
logger = logging.getLogger()

class Action(Enum):

    expires_in_days = "products-that-expire-in-10-days"
    expires_in_1_month = "products-that-expire-in-1-month"
    expires_in_3_months = "products-that-expire-in-3-months"

actions  = {

    "products-that-expire-in-10-days" : lambda x = None :offset_date_limit_in_days(10) ,
    "products-that-expire-in-1-month" : lambda x = None : offset_date_limit_in_days(30),
    "products-that-expire-in-3-months" : lambda x = None : offset_date_limit_in_days(90),
}

def offset_date_limit_in_days(days):

    return datetime.now() + timedelta(days=days)

class InputEvent(BaseModel):

    class Config:
        use_enum_values = True

    action : Action


fake_products = [
    {   
        "id_produto":1,
        "name": "Paracetamol",
        "date_valid" : "2026-06-15"
    },
    {   
        "id_produto":2,
        "name": "Diclofenaco",
        "date_valid" : "2026-07-04"
    },
    {   
        "id_produto":3,
        "name": "Dipirona",
        "date_valid" : "2026-09-01"
    }
]

def lambda_handler(event,context):

    status_code = 200
    response = None

    try:

        input_event = InputEvent(**event)
        action = input_event.action

        date_limit = actions.get(action)

        filter_product = list(filter(lambda x : datetime.strptime(x["date_valid"],"%Y-%m-%d") < date_limit(), fake_products))
        logger.info(f"Product found : {filter_product}")

        response = filter_product

    except Exception as error :

        logging.error(error)

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