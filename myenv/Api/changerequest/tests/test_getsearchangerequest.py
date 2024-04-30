import pytest
from Api.changerequest.tests.api_changerequest import Apichangerequest




@pytest.fixture
def api_changerequest():
    return Apichangerequest()


def test_getsearchangerequest_valid_data(api_changerequest):
    
    api_changerequest.paramslist 
    response = api_changerequest.get_searchangerequest()
    
    assert response.status_code == 200
    # response_json = response.json()
    # assert response_json[0]['service'] == "string"


   

def test_getsearchangerequest_invalid_token(api_changerequest):

    api_changerequest.headers['Authorization'] = 'Bearer token_invalid'
    response = api_changerequest.get_searchangerequest()
    
    
    assert response.status_code == 401

 
 
 
# def test_getsearchangerequest_wrong_value_on_field(api_changerequest):
    
#     api_changerequest.paramslist['PageNumber'] = 'okl'
#     api_changerequest.paramslist['PageSize'] = 'okm'
#     response = api_changerequest.get_searchangerequest()
#     assert response.status_code == 400       
#     assert response.json() == []  