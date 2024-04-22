import pytest
from Api.changerequest.tests.api_changerequest import Apichangerequest




@pytest.fixture
def api_changerequest():
    return Apichangerequest()

def test_postchangerequest(api_changerequest):
    
     data = {
        "name": "string",
        "holderCuid": "string",
        "holderName": "string",
        "holderEmail": "string",
        "initiatorCuid": "string",
        "initiatorName": "string",
        "initiatorEmail": "string",
        "direction": "string",
        "startDate": "2024-04-05T09:13:11.514Z",
        "priority": "string",
        "targetClient": "string",
        "sendToART": True,
        "origin": "string",
        "goal": "string",
        "reason": "string",
        "description": "string",
        "workflowDefinitionId": "string",
        "workflowInstanceId": "string",
        "status": "string",
        "reference": 0,
        "validators": "string",
        "state": 0,
        "type": 0,
        "createdDate": "2024-04-05T09:13:11.514Z",
        "kpis": [
            {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "label": "string",
                "frequency": "string",
                "unit": "string"
            }
        ]
      }
    
     response = api_changerequest.post_changerequest(data)
     assert response.status_code == 401
     
     

def test_putchangerequest(api_changerequest):
        data = {
        "name": "string",
        "holderCuid": "string",
        "holderName": "string",
        "holderEmail": "string",
        "initiatorCuid": "string",
        "initiatorName": "string",
        "initiatorEmail": "string",
        "direction": "string",
        "startDate": "2024-04-05T09:13:11.514Z",
        "priority": "string",
        "targetClient": "string",
        "sendToART": True,
        "origin": "string",
        "goal": "string",
        "reason": "string",
        "description": "string",
        "workflowDefinitionId": "string",
        "workflowInstanceId": "string",
        "status": "string",
        "reference": 0,
        "validators": "string",
        "state": 0,
        "type": 0,
        "createdDate": "2024-04-05T09:13:11.514Z",
        "kpis": [
            {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "label": "string",
                "frequency": "string",
                "unit": "string"
            }
        ]
      }
    
        response = api_changerequest.put_changerequest(data)
     
        
        assert response.status_code == 401
     
              
        
    
def test_deletechangerequest(api_changerequest):
    response = api_changerequest.delete_changerequest()
    assert response.status_code == 204




def test_getlistchangerequest(api_changerequest):
     
     response = api_changerequest.get_changerequest()
     assert response.status_code == 401
     