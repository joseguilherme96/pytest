
from lambda_local.main import call
from lambda_local.context import Context
from pytest import fixture
import src.lambda_product_expiration.handler as handler


context = Context(5)

@fixture
def event_products_that_expire_in_10_days():

    return {

        "action" : "products-that-expire-in-10-days"

    }



@fixture
def event_products_that_expire_in_1_month():

    return {

        "action" : "products-that-expire-in-1-month"

    }

@fixture
def event_products_that_expire_in_3_months():

    return {

        "action" : "products-that-expire-in-3-months"

    }

def test_event_event_products_that_expire_in_10_days(event_products_that_expire_in_10_days):

    result = call(handler.lambda_handler,event_products_that_expire_in_10_days,context)
    expected_response = ({'status_code':200,
                          'headers': {'Content-Type': 'application/json'},
                          'body': '{"Response ": [{"id_produto": 1, "name": "Paracetamol", "date_valid": "2026-06-15"}]}'},None)
    
    assert expected_response == result

def test_event_event_products_that_expire_in_1_month(event_products_that_expire_in_1_month):

    result = call(handler.lambda_handler,event_products_that_expire_in_1_month,context)
    expected_response = ({'status_code':200,
                          'headers': {'Content-Type': 'application/json'},
                          'body': '{"Response ": [{"id_produto": 1, "name": "Paracetamol", "date_valid": "2026-06-15"}, {"id_produto": 2, "name": "Diclofenaco", "date_valid": "2026-07-04"}]}'},None)
    
    assert expected_response == result

def test_event_event_products_that_expire_in_3_months(event_products_that_expire_in_3_months):

    result = call(handler.lambda_handler,event_products_that_expire_in_3_months,context)
    expected_response = ({'status_code':200,
                          'headers': {'Content-Type': 'application/json'},
                          'body': '{"Response ": [{"id_produto": 1, "name": "Paracetamol", "date_valid": "2026-06-15"}, {"id_produto": 2, "name": "Diclofenaco", "date_valid": "2026-07-04"}, {"id_produto": 3, "name": "Dipirona", "date_valid": "2026-09-01"}]}'},None)
    
    assert expected_response == result