import pytest
from Api.changerequest.testsfonc.api_changerequest import Apichangerequest




@pytest.fixture
def api_changerequest():
    return Apichangerequest()



def test_deletechangerequest_valid_data(api_changerequest):
 response = api_changerequest.delete_changerequest()
 assert response.status_code == 204


def test_deletechangerequest_invalid_token(api_changerequest):
  api_changerequest.headers['Authorization'] = 'Bearer token_invalid'
  response = api_changerequest.delete_changerequest()
  assert response.status_code == 401


def test_deletechangerequest_no_value_invalid_token(api_changerequest):
  api_changerequest.headers['Authorization'] = ''
  response = api_changerequest.delete_changerequest()
  assert response.status_code == 401
    
def test_deletechangerequest_wrong_data_type_value_on_field_id(api_changerequest):
    api_changerequest.idelete = '23074633-2087-40af-'
    response = api_changerequest.delete_changerequest()
    assert response.status_code == 404


def test_deletechangerequest_no_value_on_field_id(api_changerequest):
    api_changerequest.idelete = ''
    response = api_changerequest.delete_changerequest()
    assert response.status_code == 405
    
    
def test_deletechangerequest_wrong_value_on_field_id(api_changerequest):
    api_changerequest.idelete = 'e5461c74-e1ed-4d8c-abe6-53740e92b560'
    response = api_changerequest.delete_changerequest()
    assert response.status_code == 404