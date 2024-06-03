import pytest
from Api.workpackage.testsfonc.api_workpackage import Apiworkpackage




@pytest.fixture
def api_workpackage():
    return Apiworkpackage()


def test_getworkpackage_valid_data(api_workpackage):
    
    
   response = api_workpackage.get_workpackage()
   assert response.status_code == 200



def test_getworkpackage_invalid_token(api_workpackage):

    api_workpackage.headers['Authorization'] = 'Bearer token_invalid'
    response = api_workpackage.get_workpackage()
    assert response.status_code == 401



def test_getworkpackage_no_value_token(api_workpackage):

    api_workpackage.headers['Authorization'] = ''
    response = api_workpackage.get_workpackage()
    assert response.status_code == 401
 


    
    
