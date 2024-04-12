import pytest
import requests
import json
from config import AUTHORIZATION_TOKEN
from config import BASE_URL


def test_putchange():
    
    headerPut = {
        'accept':'application/json',
        'Content-Type':'application/json',
        'Authorization': AUTHORIZATION_TOKEN
    }
    
    url = f"{BASE_URL}/253c0afd-19bf-4bd7-8ce8-8705e006d91c"
    
    request_body = {
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
        "state": 10,
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
    
   
    response = requests.put(url , headers = headerPut, json = request_body, verify=False )  # Remplacez par votre URL d'API
    
    
    assert response.status_code == 204
    