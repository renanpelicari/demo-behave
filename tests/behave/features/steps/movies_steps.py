from behave import when, then
from config import API_URL

import requests

MOVIES_ENDPOINT = f"{API_URL}/api/v1/movies"

@when('I request all movies')
def get_movies(context):
    context.response = requests.get(MOVIES_ENDPOINT)

@when('I request movie with id {movie_id}')
def get_movie_by_id(context, movie_id):
    context.response = requests.get(f"{MOVIES_ENDPOINT}/{movie_id}")

@when("I create a movie with:")
def create_movie(context):
    payload = {row['key']: row['value'] for row in context.table}
    context.response = requests.post(MOVIES_ENDPOINT, json=payload)

@when("I update movie with id {movie_id} with:")
def update_movie(context, movie_id):
    payload = {row['key']: row['value'] for row in context.table}
    context.response = requests.put(f"{MOVIES_ENDPOINT}/{movie_id}", json=payload)

@when('I delete movie with id {movie_id}')
def delete_movie(context, movie_id):
    context.response = requests.delete(f"{MOVIES_ENDPOINT}/{movie_id}")

@then('the response should contain "{movie_name}"')
def validate_movie_name(context, movie_name):
    assert any(movie_name in m['name'] for m in context.response.json())

@then('the response should not contain "{movie_name}"')
def validate_movie_not_in_list(context, movie_name):
    assert all(movie_name not in m['name'] for m in context.response.json())

@then('the response should contain the following movies:')
def validate_list_of_movies(context):
    expected_movies = [row['name'] for row in context.table]
    response_movies = [movie['name'] for movie in context.response.json()]
    for movie in expected_movies:
        assert movie in response_movies

@then("the response should contain:")
def validate_response_body(context):
    expected_data = {row['key']: row['value'] for row in context.table}
    response_data = context.response.json()
    for key, value in expected_data.items():
        assert str(response_data.get(key)) == value


