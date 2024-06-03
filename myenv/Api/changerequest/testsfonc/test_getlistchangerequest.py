import pytest
from Api.changerequest.testsfonc.api_changerequest import Apichangerequest




@pytest.fixture
def api_changerequest():
    return Apichangerequest()


def test_getlistchangerequest_valid_data(api_changerequest):
    
    
   response = api_changerequest.get_listchangerequest()
  
#    response_json = response.json()
#    assert isinstance(response_json, list) and len(response_json) > 0
   assert response.status_code == 200
#    assert response_json[0]['state'] == 0


def test_getlistchangerequest_invalid_token(api_changerequest):

    api_changerequest.headers['Authorization'] = 'Bearer token_invalid'
    response = api_changerequest.get_listchangerequest()
    assert response.status_code == 401



def test_getlistchangerequest_no_value_token(api_changerequest):

    api_changerequest.headers['Authorization'] = ''
    response = api_changerequest.get_listchangerequest()
    assert response.status_code == 401
 


    
    
