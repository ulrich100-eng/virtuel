import pytest
import concurrent.futures
import time
from   Api.changerequest.testsf.api_change import Apichange






@pytest.fixture
def api_change():
    return Apichange()
   
@pytest.mark.parametrize("num_requests", [1, 100, 1000])


@pytest.mark.performance
def test_api_performance(num_requests):
    if num_requests == 1:
        normal_load_scenario(api_change)
    # elif num_requests == 100:
    #     high_load_scenario()
    # elif num_requests == 1000:
    #     max_load_scenario()
    
    
def test_send_post(api_change):

    api_change = Apichange()  # Création d'une instance de la classe Apichange


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
    
    start_time = time.time()
    response = api_change.post_changerequestperf(data)
    end_time = time.time()
    response_time = end_time - start_time
    print("Temps  d'exécution d'une requete:", response_time)
    is_success = response.status_code == 200
    return response_time, is_success


def normal_load_scenario(api_change):
    success_count = 0
    total_time = 0
    failure_count = 0 
    throughput = 0
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(test_send_post,api_change) for _ in range(1)]

        for future in concurrent.futures.as_completed(futures):
            response_time, is_success = future.result()
            total_time += response_time
            print("Temps total  d'exécution :", total_time)
            if is_success:
                success_count += 1
              
            else:
                failure_count += 1
                
#      # Calcul du temps de réponse moyen
    average_response_time = total_time / 1
    print(f"Temps de réponse moyen : {average_response_time} secondes")
    
    # Calcul du débit (requêtes par seconde)
    throughput = success_count / total_time  
    print(f"Le debit : {throughput}")
     
      # Calcul du taux de succès et d'échec
    
    success_rate = (success_count / 1) * 100
    
    print(f"Taux de succès : {success_rate}%")
    
    
    failure_rate = (failure_count / 1) * 100
    print(f"Taux d'échec : {failure_rate}%")
     
    assert success_count == 1, "Not all requests succeeded"
    assert average_response_time < 1, f"Average response time exceeded 1 second: {average_response_time} seconds"
















