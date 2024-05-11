import pytest
from Api.changerequest.tests.api_changerequest import Apichangerequest




@pytest.fixture
def api_changerequest():
    return Apichangerequest()


def test_postchangerequest_valid_data(api_changerequest):
    
    
    # api_changerequest  = Apichangerequest()
    
    data = {        
            
  "name": "string",
  "holderCuid": "string",
  "holderName": "string",
  "holderEmail": "string",
  "initiatorCuid": "string",
  "initiatorName": "string",
  "initiatorEmail": "string",
  "direction": "string",
  "department": "string",
  "service": "string",
  "startDate": "2024-05-11T15:12:21.426Z",
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
  "createdDate": "2024-05-11T15:12:21.426Z",
  "kpis": [
    {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "label": "string",
      "frequency": 0,
      "unit": "string"
    }
  ]

 }
    
    response = api_changerequest.post_changerequest(data)
    assert response.status_code == 201





def test_postchangerequest_invalid_token(api_changerequest):
   
    
   
    data = { 
        "name": "string",
        "holderCuid": "string",
        "holderName": "string",
        "holderEmail": "string",
        "initiatorCuid": "string",
        "initiatorName": "string",
        "initiatorEmail": "string",
        "direction": "string",
        "startDate": "2024-04-29T10:37:01.701Z",
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
        "createdDate": "2024-04-29T10:37:01.701Z",
        "kpis": [
            {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "label": "string",
                "frequency": 0,
                "unit": "string"
            }
        ]
    }

    api_changerequest.headers['Authorization'] = 'Bearer token_invalid'
    response = api_changerequest.post_changerequest(data)
    assert response.status_code == 401



def test_postchangerequest_no_token(api_changerequest):
   
    
   
    data = { 
        "name": "string",
        "holderCuid": "string",
        "holderName": "string",
        "holderEmail": "string",
        "initiatorCuid": "string",
        "initiatorName": "string",
        "initiatorEmail": "string",
        "direction": "string",
        "startDate": "2024-04-29T10:37:01.701Z",
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
        "createdDate": "2024-04-29T10:37:01.701Z",
        "kpis": [
            {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "label": "string",
                "frequency": 0,
                "unit": "string"
            }
        ]
    }

    api_changerequest.headers['Authorization'] = ''
    response = api_changerequest.post_changerequest(data)
    assert response.status_code == 401

 
 
 
def test_postchangerequest_value_error_on_field_name(api_changerequest):
    
    data = { 
        "name": 2,
        "holderCuid": "string",
        "holderName": "string",
        "holderEmail": "string",
        "initiatorCuid": "string",
        "initiatorName": "string",
        "initiatorEmail": "string",
        "direction": "string",
        "startDate": "2024-04-29T10:37:01.701Z",
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
        "createdDate": "2024-04-29T10:37:01.701Z",
        "kpis": [
            {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "label": "string",
                "frequency": 0,
                "unit": "string"
            }
        ]
    }
    
    response = api_changerequest.post_changerequest(data)
    assert response.status_code == 400       
    
    


def test_postchangerequest_value_error_on_state_field(api_changerequest):
    
    
   
    data = { 
        "name": "string",
        "holderCuid": "string",
        "holderName": "string",
        "holderEmail": "string",
        "initiatorCuid": "string",
        "initiatorName": "string",
        "initiatorEmail": "string",
        "direction": "string",
        "startDate": "2024-04-29T10:37:01.701Z",
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
        "state": "10",
        "type": 0,
        "createdDate": "2024-04-29T10:37:01.701Z",
        "kpis": [
            {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "label": "string",
                "frequency": 0,
                "unit": "string"
            }
        ]
    }
    
    response = api_changerequest.post_changerequest(data)
    assert response.status_code == 400
    
 
 
    
def test_postchangerequest_no_value_on_state_field(api_changerequest):
    
    
   
    data = { 
        "name": "string",
        "holderCuid": "string",
        "holderName": "string",
        "holderEmail": "string",
        "initiatorCuid": "string",
        "initiatorName": "string",
        "initiatorEmail": "string",
        "direction": "string",
        "startDate": "2024-04-29T10:37:01.701Z",
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
        "state": '' ,
        "type": 0,
        "createdDate": "2024-04-29T10:37:01.701Z",
        "kpis": [
            {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "label": "string",
                "frequency": 0,
                "unit": "string"
            }
        ]
    }
    
    response = api_changerequest.post_changerequest(data)
    assert response.status_code == 400
        