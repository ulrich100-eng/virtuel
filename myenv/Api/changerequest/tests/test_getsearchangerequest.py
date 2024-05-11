import pytest
from Api.changerequest.tests.api_changerequest import Apichangerequest




@pytest.fixture
def api_changerequest():
    return Apichangerequest()


def test_getsearchangerequest_valid_data(api_changerequest):
    
   
    response = api_changerequest.get_searchangerequest()
    
    assert response.status_code == 200
    


   

def test_getsearchangerequest_invalid_token(api_changerequest):

    api_changerequest.headers['Authorization'] = 'Bearer token_invalid'
    response = api_changerequest.get_searchangerequest()
    
    
    assert response.status_code == 401



def test_getsearchangerequest_no_token(api_changerequest):

    api_changerequest.headers['Authorization'] = 'Bearer token_invalid'
    response = api_changerequest.get_searchangerequest()
    
    
    assert response.status_code == 401
 
 
 
def test_getsearchangerequest_wrong_value_on_field_pagesize(api_changerequest):
    
   
    api_changerequest.pa['PageSize'] = 'ocm'
    response = api_changerequest.get_searchangerequest()
    assert response.status_code == 400       
   
   
def test_getsearchangerequest_wrong_value_on_field_pagenumber(api_changerequest):
    
   
    api_changerequest.paramslist['PageSize'] = 'ocm'
    response = api_changerequest.get_searchangerequest()
    assert response.status_code == 400      
    
    
def test_getsearchangerequest_no_value_on_field_pagenumber(api_changerequest):
    
    api_changerequest.paramslist['PageNumber'] = ''
   
    response = api_changerequest.get_searchangerequest()
    assert response.status_code == 400       
    
    
    
def test_getsearchangerequest_no_value_on_field_pagesize(api_changerequest):
    
    
    api_changerequest.paramslist['PageSize'] = ''
    response = api_changerequest.get_searchangerequest()
    assert response.status_code == 400       
    