from behave import when, then
from api_steps import API_URL
import requests

@when("I request all books")
def find_books(context):
    context.response = requests.get(f"{API_URL}/api/v1/books")

@then("the response should contain the following books:")
def validate_list_of_books(context):
    expected_books = [row['name'] for row in context.table]
    response_books = [book['name'] for book in context.response.json()]
    for book in expected_books:
        assert book in response_books