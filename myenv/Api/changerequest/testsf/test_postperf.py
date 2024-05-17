import pytest
from Api.changerequest.testsf.api_change import Apichange
from statistics import mean
import time






@pytest.fixture
def api_change():
    return Apichange()


def test_postchangerequest_valid(api_change):
    
    
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
    
    num_requests = 10
    response_times = []
    success_count = 0
    failure_count = 0
    
    
    
    for _ in range(num_requests):
        
        start_time = time.time()
        response = api_change.post_changerequestperf(data)
        end_time = time.time()
        response_time = end_time - start_time
        print("Temps  d'exécution :", response_time)
        
        
        response_times.append(response_time)
        print(f"Respnse : {response_times} secondes")
        avg_time = mean(response_times)
        print(f"Temps de réponse moyen : {avg_time} secondes")
        
        
        if response.status_code == 200:
            success_count += 1
        else :
            failure_count += 1 
            print(f"Failure : {failure_count}")
       
    throughput = num_requests / sum(response_times)
    print(f"Le debit : {throughput}")
    
    
    success_rate = (success_count / num_requests) * 100
    print(f"Taux de succès : {success_rate}%")
     
     
    failure_rate = (failure_count / num_requests) * 100
    print(f"Taux d'échec : {failure_rate}%")
    
    
    # assert success_rate == 100, "All requests should succeed"
    # assert success_count == 10
    assert avg_time < 1, f"Average response time exceeded 1 second: {avg_time} secondes"