from behave import then

@then('the response status should be {status_code:d}')
def validate_response_code(context, status_code):
    assert context.response.status_code == status_code