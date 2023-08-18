from rest_framework import status
import pytest
import responses
import requests


# Test for authorized access to list views
@pytest.mark.parametrize("url",[
                                ('http://127.0.0.1:8000/api/restaurant/'),
                                ('http://127.0.0.1:8000/api/menu/'),
                                ('http://127.0.0.1:8000/api/employee/')
                               ])
def test_list_view_authorized(test_get_token,url):
    # Simulate successful GET request and restricted POST, PATCH, DELETE requests
    responses.add(method=responses.GET, url=url, status=200)
    responses.add(method=responses.POST, url=url, status=403)
    responses.add(method=responses.PATCH, url=url, status=403)
    responses.add(method=responses.DELETE, url=url, status=403)

    headers = {
        'Authorization': f'Bearer {test_get_token["access"]}',
        'Other-Header': 'Value'
    }
    
    assert requests.get(url, headers=headers).status_code == status.HTTP_200_OK
    assert requests.post(url, headers=headers).status_code == status.HTTP_403_FORBIDDEN
    assert requests.patch(url, headers=headers).status_code == status.HTTP_403_FORBIDDEN
    assert requests.delete(url, headers=headers).status_code == status.HTTP_403_FORBIDDEN


# Test for authorized access to list views
@pytest.mark.parametrize("url",[
                                ('http://127.0.0.1:8000/api/restaurant/1/'),
                                ('http://127.0.0.1:8000/api/menu/1/'),
                                ('http://127.0.0.1:8000/api/employee/1/')
                               ])
def test_updated_estroy_view_authorized(test_get_token,url):
    # Simulate successful GET request and restricted POST, PATCH, DELETE requests
    responses.add(method=responses.GET, url=url, status=403)
    responses.add(method=responses.POST, url=url, status=403)
    responses.add(method=responses.PATCH, url=url, status=403)
    responses.add(method=responses.DELETE, url=url, status=403)

    headers = {
        'Authorization': f'Bearer {test_get_token["access"]}',
        'Other-Header': 'Value'
    }
    
    assert requests.get(url, headers=headers).status_code == status.HTTP_403_FORBIDDEN
    assert requests.post(url, headers=headers).status_code == status.HTTP_403_FORBIDDEN
    assert requests.patch(url, headers=headers).status_code == status.HTTP_403_FORBIDDEN
    assert requests.delete(url, headers=headers).status_code == status.HTTP_403_FORBIDDEN


# Test for unauthorized access to list views
@pytest.mark.parametrize("url",[
                                ('http://127.0.0.1:8000/api/restaurant/'),
                                ('http://127.0.0.1:8000/api/menu/'),
                                ('http://127.0.0.1:8000/api/employee/')
                               ])
def test_list_view_unauthorized(url):
    # Simulate successful GET request and restricted POST, PATCH, DELETE requests
    assert requests.get(url).status_code == status.HTTP_200_OK
    assert requests.post(url).status_code == status.HTTP_401_UNAUTHORIZED
    assert requests.patch(url).status_code == status.HTTP_401_UNAUTHORIZED
    assert requests.delete(url).status_code == status.HTTP_401_UNAUTHORIZED


# Test for unauthorized access to list views
@pytest.mark.parametrize("url",[
                                ('http://127.0.0.1:8000/api/restaurant/1/'),
                                ('http://127.0.0.1:8000/api/menu/1/'),
                                ('http://127.0.0.1:8000/api/employee/1/')
                               ])
def test_updated_estroy_view_unauthorized(url):
    # Simulate successful GET request and restricted POST, PATCH, DELETE requests
    assert requests.get(url).status_code == status.HTTP_401_UNAUTHORIZED
    assert requests.post(url).status_code == status.HTTP_401_UNAUTHORIZED
    assert requests.patch(url).status_code == status.HTTP_401_UNAUTHORIZED
    assert requests.delete(url).status_code == status.HTTP_401_UNAUTHORIZED


# Test for unauthorized access to "top menu" endpoints
@pytest.mark.parametrize("url",[
                                ('http://127.0.0.1:8000/api/today/menu/'),
                                ('http://127.0.0.1:8000/api/today/top/')
                               ])
def test_top_menu(test_get_token,url):
    # Simulate restricted access to "top menu" endpoints
    responses.add(method=responses.GET, url=url, status=403)

    headers = {
        'Authorization': f'Bearer {test_get_token["access"]}',
        'Other-Header': 'Value'
    }
    
    assert requests.get(url, headers=headers).status_code == status.HTTP_403_FORBIDDEN


# Test token refresh
def test_token_refresh(test_get_token,test_create_user):
    # Test token refresh using POST request
    assert requests.post(f'http://127.0.0.1:8000/api/token/?refresh={test_get_token}', data=test_create_user).status_code == status.HTTP_200_OK

