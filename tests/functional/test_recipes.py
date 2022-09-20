
# Test web app home page
def test_swagger_page(test_client):
    """
    GIVEN Surfers API Web Service
    WHEN the '/api/v1/' page is requested (GET)
    THEN check that the response is valid
    """
    _response = test_client.get('/api/v1/')
    assert _response.status_code == 200
    assert b'Weather and Surf Forecast REST API' in _response.data
    assert b'swaggerui' in _response.data

# Test against the health check page to ensure ok response
def test_healthcheck_page(test_client):
    """
    GIVEN Service health check web page
    WHEN the '/api/v1/healthz' page is requested (GET)
    THEN check that all responses are valid and healthy
    """
    _response = test_client.get('/api/v1/healthz')
    assert _response.status_code == 200
    assert b'health' in _response.data
    assert b'ok' in _response.data

# Test that the 404 error condition is caught
def test_unknown_page(test_client):
    """
    GIVEN An unknown web page to ensure 404 caught
    WHEN the '/unknown' page is requested (GET)
    THEN check that the error is raised
    """
    
    _response = test_client.get('/unknown')
    assert _response.status_code == 404
    assert b"swagger" not in _response.data
