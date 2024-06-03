import pytest
from Api.changerequest.testsfonc.api_changerequest import Apichangerequest




@pytest.fixture
def api_changerequest():
    return Apichangerequest()


def test_putchangerequestclose_valid_data(api_changerequest):
    
   
    response = api_changerequest.put_changerequestclose()
    
    assert response.status_code == 204
    


   

def test_putchangerequestclose_invalid_token(api_changerequest):

    api_changerequest.headers1['Authorization'] = 'Bearer token_invalid'
    response = api_changerequest.put_changerequestclose()
    
    
    assert response.status_code == 401




def test_putchangerequestclose_no_token(api_changerequest):

    api_changerequest.headers1['Authorization'] = ''
    response = api_changerequest.put_changerequestclose()
    
    
    assert response.status_code == 401
 
 
 
def test_putchangerequestclose_wrong_value_on_field_id(api_changerequest):
    
   
    api_changerequest.idputclose = 'close?id=e5461c74-e1ed-4d8c-abe6-53740e92b560'
    response = api_changerequest.put_changerequestclose()
    assert response.status_code == 404       
   
   
   
def test_putchangerequestclose_wrong_data_type_on_field_id(api_changerequest):
    
    
    api_changerequest.idputclose = 'close?id=e5461c74-e1ed-'
    
    response = api_changerequest.put_changerequestclose()
    
    assert response.status_code == 400     
    
    
    
    
def test_putchangerequestclose_no_value_on_field_id(api_changerequest):
    
    api_changerequest.idputclose = 'close?id='
   
    response = api_changerequest.put_changerequestclose()
    assert response.status_code == 400       
    
    
 