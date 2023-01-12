from assertpy import assert_that, soft_assertions
from utils.request import Response
import requests

from cerberus import Validator


# Validate HTTP status code
def assert_status_code_ok(response: Response):
    assert_that(response.status_code, description=response.description).is_equal_to(requests.codes.ok)


def assert_status_code_created(response: Response):
    assert_that(response.status_code, description=response.description).is_equal_to(requests.codes.created)


def assert_status_code_unauthorized(response: Response):
    assert_that(response.status_code, description=response.description).is_equal_to(requests.codes.unauthorized)


def assert_status_code_bad_request(response: Response):
    assert_that(response.status_code, description=response.description).is_equal_to(requests.codes.bad_request)


def assert_status_code_not_found(response: Response):
    assert_that(response.status_code, description=response.description).is_equal_to(requests.codes.not_found)


# Validate HTTP Response
def assert_response_contains_value(response_data, field_name, field_value):
    if isinstance(response_data, list):
        assert_that(response_data).extracting(field_name).is_not_empty().contains(field_value)

    elif isinstance(response_data, dict):
        assert_that(response_data[field_name]).is_equal_to(field_value)


# # Validate Response schema
# def validate_schema(schema, response: Response):
#     validator = Validator(schema, require_all=True)
#     if response
#     with soft_assertions():
#         for person in persons:
#             is_valid = validator.validate(person)
#             assert_that(is_valid, description=validator.errors).is_true()
