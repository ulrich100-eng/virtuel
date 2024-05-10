import pytest
import requests
import random
import time
from   Api.changerequest.testsf.api_change import Apichange







@pytest.fixture
def api_change():
    return Apichange()
   
    

def test_send_post(api_change):
       
    api_change = Apichange
    
    request_body = {
        
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
    

    # Nombre de requêtes à envoyer pour le test de performance
    num_requests = 50

    # Initialisation des métriques
    total_time = 0
    success_count = 0
    failure_count = 0
    # total_time = time.time()

    # Envoi de plusieurs requêtes et mesure des métriques de performance
    for _ in range(num_requests):
        start_time = time.time()
        response = api_change.send_post_request(request_body)
        assert response.status_code == 200
        end_time = time.time()
        
        print("Les métriques de performance sont :")
        # Calcul du temps de réponse
        response_time = end_time - start_time
        total_time += response_time
        print("Temps total d'exécution:", total_time)
        
        # Vérification du succès ou de l'échec de la requête de manière aléatoire
        random_value = random.random()
        print("Valeur aléatoire générée :", random_value)
        if random.random() < 0.9:  # Taux de succès de 90%
            assert response.status_code == 200
            success_count += 1
        else:
            assert response.status_code != 200
            failure_count += 1

    # Calcul du temps de réponse moyen
        average_response_time = total_time / num_requests
        
        # print("Temps de reponse moyen : " , average_response_time ) 
        
        print(f"Temps de réponse moyen : {average_response_time} secondes")
        
    # Calcul du taux de succès et d'échec
    
        success_rate = success_count / num_requests
        print(f"Taux de succès : {success_rate}")
    
        failure_rate = failure_count / num_requests
        print(f"Taux d'échec : {failure_rate}")
    
    # Assertion pour vérifier si le temps de réponse moyen est inférieur à 1 seconde
    assert average_response_time < 1, f"Average response time exceeded 1 second: {average_response_time} seconds"

  

    

















