from lambda_local.main import call
from lambda_local.context import Context
import src.lambda_calculator.handler as handler

context = Context(5)

def test_lambda_handler_event_plus(event_plus):

    result = call(handler.lambda_handler, event_plus, context)
    expected_response = ({'status_code':200,
                          'headers': {'Content-Type': 'application/json'},
                          'body': '{"Response ": "4 plus 4 = 8"}'},None)
    assert result == expected_response

def test_lambda_handler_event_minus(event_minus):

    result = call(handler.lambda_handler, event_minus, context)
    expected_response = ({'status_code':200,
                          'headers': {'Content-Type': 'application/json'},
                          'body': '{"Response ": "5 minus 4 = 1"}'},None)
    assert result == expected_response

def test_lambda_handler_event_times(event_times):

    result = call(handler.lambda_handler, event_times, context)
    expected_response = ({'status_code':200,
                          'headers': {'Content-Type': 'application/json'},
                          'body': '{"Response ": "5 times 4 = 20"}'},None)
    assert result == expected_response

def test_lambda_handler_event_divided_by(event_divided_by):

    result = call(handler.lambda_handler, event_divided_by, context)
    expected_response = ({'status_code':200,
                          'headers': {'Content-Type': 'application/json'},
                          'body': '{"Response ": "30 divided-by 10 = 3.0"}'},None)
    assert result == expected_response

def test_lambda_handler_event_divided_by_zero(event_divided_by_zero):

    result = call(handler.lambda_handler, event_divided_by_zero, context)
    expected_response = ({'status_code':200,
                          'headers': {'Content-Type': 'application/json'},
                          'body': '{"Response ": "I can\'t divide 30 by 0!"}'},None)
    assert result == expected_response

def test_lambda_handler_event_validation_error(event_validation_error):

    result = call(handler.lambda_handler, event_validation_error, context)
    expected_response = ({'status_code':400,
                          'headers': {'Content-Type': 'application/json'},
                          'body': '{"Response ": [{"loc": ["x"], "msg": "value is not a valid integer", "type": "type_error.integer"}, {"loc": ["y"], "msg": "value is not a valid integer", "type": "type_error.integer"}]}'},None)
    assert result == expected_response

def test_lambda_handler_event_exception(event_exception,mocker):

    mocker.patch("src.lambda_calculator.handler.InputEvent", side_effect=Exception("Internal Server Error Occured"))

    response_direto = handler.lambda_handler(event_exception, context)
    result = (response_direto, None)

    expected_response = ({'status_code':500,
                          'headers': {'Content-Type': 'application/json'},
                          'body': '{"Response ": "Internal Server Error Occured"}'},None)
    assert result == expected_response