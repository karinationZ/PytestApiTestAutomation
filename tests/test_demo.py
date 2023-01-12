'''
1. Verify GET request to retrieve article information
2. Verify GET request to retrieve list of articles
3. Verify POST request to create a new article
4. Verify PUT request to update existing article
5. Verify DELETE request to remove existing article
6. Verify GET parameter validation for an article request
7. Verify POST parameter validation for an article request
8. Verify response data integrity of an article request
9. Verify authorization header support for an article request
10. Verify response status code validity for all type of requests
'''
from validators.assertions import *


def test_get_collections(demo_client):
    response = demo_client.get_users()
    assert_status_code_ok(response)
    assert_response_contains_value(response.body['data'], 'id', 4429)
