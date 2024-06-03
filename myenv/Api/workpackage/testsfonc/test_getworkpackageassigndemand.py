import pytest
from Api.workpackage.testsfonc.api_workpackage import Apiworkpackage




@pytest.fixture
def api_workpackage():
    return Apiworkpackage()


def test_getworkpackagassigndemand_valid_data_with_role_admin_global(api_workpackage):
    
    
   response = api_workpackage.get_workpackageassigndemand()
  
   assert response.status_code == 200



def test_getworkpackagassigndemand_invalid_token(api_workpackage):

    api_workpackage.headers['Authorization'] = 'Bearer token_invalid'
    response = api_workpackage.get_workpackageassigndemand()
    assert response.status_code == 401



def test_getworkpackagassigndemand_no_value_token(api_workpackage):

    api_workpackage.headers['Authorization'] = ''
    response = api_workpackage.get_workpackageassigndemand()
    assert response.status_code == 401
 