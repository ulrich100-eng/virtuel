import pytest
from Api.changerequest.tests.api_changerequest import Apichangerequest




@pytest.fixture
def api_changerequest():
    return Apichangerequest()


def test_putchangerequest_valid_data(api_changerequest):
    
    
    
    data = {
         
        "name": "ocm",
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
    
    response = api_changerequest.put_changerequest(data)
    assert response.status_code == 204





def test_putchangerequest_invalid_token(api_changerequest):
    
    
   
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
    response = api_changerequest.put_changerequest(data)
    assert response.status_code == 401

 
 
def test_putchangerequest_no_value_token(api_changerequest):
    
    
   
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
    response = api_changerequest.put_changerequest(data)
    assert response.status_code == 401

 
 
def test_putchangerequest_value_error_on_field_name(api_changerequest):
   
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
    
    response = api_changerequest.put_changerequest(data)
    assert response.status_code == 400       
    
    


def test_putchangerequest_value_error_on_state_field(api_changerequest):
    
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
        "state": 10,
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
    
    response = api_changerequest.put_changerequest(data)
    assert response.status_code == 400
    


def test_putchangerequest_no_value_on_state_field(api_changerequest):
    
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
        "state": '',
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
    
    response = api_changerequest.put_changerequest(data)
    assert response.status_code == 400
        
    
    
def test_putchangerequest_wrong_value_on_field_id(api_changerequest):
 
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
    api_changerequest.idput = 'e5461c74-e1ed-4d8c-abe6-53740e92b560'
    response = api_changerequest.put_changerequest(data)
    assert response.status_code == 500




def test_putchangerequest_wrong_data_type_on_field_id(api_changerequest):
   
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
        "state": 10,
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
    api_changerequest.idput = '11a34b52-e03b'
    response = api_changerequest.put_changerequest(data)
    assert response.status_code == 404





def test_putchangerequest_no_value_on_field_id(api_changerequest):
   
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
        "state": 10,
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
    api_changerequest.idput = ''
    response = api_changerequest.put_changerequest(data)
    assert response.status_code == 405