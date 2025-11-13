from behave import then

API_URL = "http://127.0.0.1:8000"

@then('the response status should be {status_code:d}')
def validate_response_code(context, status_code):
    assert context.response.status_code == status_code