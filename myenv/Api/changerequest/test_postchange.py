import pytest
import requests
import json

def test_postchange():
    
    header = {
        'accept':'application/json',
        'Content-Type':'application/json',
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJrSnRxNGNzNkRJRllNZFJ0TFMzeE5EcTNFN0M3UzBnWlVOeUZMQmYwZjVVIn0.eyJleHAiOjE3MTI2NjIyMjYsImlhdCI6MTcxMjY2MTMyNiwiYXV0aF90aW1lIjoxNzEyNjYxMzI1LCJqdGkiOiI3MGUxN2RkZi0zZmUyLTQwNjgtODk0MC0yN2I3MTEyMDk2YWIiLCJpc3MiOiJodHRwczovL2tleWNsb2FrLXByZXByb2QuYXBwcy5kZXYub3JhbmdlLmxvY2FsL3JlYWxtcy9kaWdpdGFsLWFwcCIsImF1ZCI6InBlcmZpdCIsInN1YiI6IjA0OWU0YjUxLWVhNWUtNDMxYy04ZTEwLTJlZmQ3OWE4YWIxMiIsInR5cCI6IklEIiwiYXpwIjoicGVyZml0Iiwibm9uY2UiOiI5ZTRjMGY2ZS1lN2IwLTRkOTctYjJhMC1iZWRhM2M2Y2Y4OTAiLCJzZXNzaW9uX3N0YXRlIjoiNmEwYzMxOWMtMDU3MS00M2UxLWJhNDktNDYyMjIzNDg5Njk0IiwiYXRfaGFzaCI6InVLbmRDanpjODhMazRwQ1ljZ1dadVEiLCJzaWQiOiI2YTBjMzE5Yy0wNTcxLTQzZTEtYmE0OS00NjIyMjM0ODk2OTQiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJLRU5HTkUgIEtFTkdORSIsInByZWZlcnJlZF91c2VybmFtZSI6InpiaHE4MzQ5IiwiZ2l2ZW5fbmFtZSI6IktFTkdORSAiLCJmYW1pbHlfbmFtZSI6IktFTkdORSIsImVtYWlsIjoidWxyaWNoLmtlbmduZUBvcmFuZ2UuY29tIn0.ZVpUWti9heHuUwD3Q1dR129paxPQVOwmRb6yYD1zIMx_tvoeqPg6N5VSc4S5QeOjEARChfQq35felNHhh-X_-nMdVqeYplGGMH4DRgw6RfNflddaV8kSZAeV5V1Ak7Rg8F76lZY_wRc0rwARb8uAiRNNi47mauSOzEGC-5q9Ew4m45c89C0LW2kgqqu5mWj0UaaZdJpxrkeNlCrEjeBRKf194k-ypw1_2k6bemIqRliuX9rY3Jekku5N9qZn7DLgJ7a8HbLJ2oiVcdCab89Xq7Jsu0AhjBFnTYq4Ymo67dd6TGoMQK3tTZZyUL-JJzdXEnlOQNDXVdHEHMGlskKK5w'
    }
    
    url = 'https://change-request.perfit.apps.dev.orange.local/api/changerequests'
    
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
    
   
    response = requests.post(url , headers = header, json = request_body, verify=False )  # Remplacez par votre URL d'API
    
    
    assert response.status_code == 401
    