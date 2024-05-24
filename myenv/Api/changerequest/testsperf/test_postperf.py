import pytest
import time
import concurrent.futures  
from Api.changerequest.testsperf.api_changeperf import Apichange  # Assurez-vous que le chemin est correct





def run(nb):
    
    api_change = Apichange()
    # Vous pouvez ajuster ce nombre selon vos besoins
    # Corps de la requête à envoyer
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
    
    
    print(f"Received nb: {nb}")  # Vérifiez que nb est correctement reçu
    
    data_list = [data for _ in range(nb)] 
    
    failure_count = 0 
    success_count = 0
    
    
    
    start_time = time.time()  # Temps de départ
    print(f"Running test with {nb} requests")  # Impression pour débogage
    
    # Exécution des requêtes en parallèle avec ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=nb) as executor:
            # Map les données avec les requêtes et stocke les résultats
        results = list(executor.map(lambda data: api_change.post_changeperf(data), data_list))
    end_time = time.time()  # Temps de fin
    
    # response_times = []  # Liste pour stocker les temps de réponse de chaque requête

    for result in results:
            response_time = result.elapsed.total_seconds() 
            print("Temps de reponse d'une requete :", response_time)# Temps de réponse en secondes
            # response_times.append(response_time)

            if result.status_code == 201:
                success_count += 1
            else:
                failure_count += 1

    total_time = end_time - start_time  # Temps total d'exécution
    print("Temps total d'exécution :", total_time)
            
    average_response_time = total_time / nb
    print(f"Temps de réponse moyen : {average_response_time} secondes")
    
    
          # Calcul du taux de succès et d'échec
    
    success_rate = (success_count / nb) * 100
    
    print(f"Taux de succès : {success_rate}%")
    
    
    failure_rate = (failure_count / nb) * 100
    print(f"Taux d'échec : {failure_rate}%")
    
    # Calcul du débit (requêtes par seconde)
    throughput = nb / total_time  
    print(f"Le debit : {throughput}")
    
    
    # Assertions pour les requêtes légères (nb = 10)
    if nb == 10:
        assert average_response_time < 0.5, f"Temps de réponse moyen élevé: {average_response_time} secondes pour {nb} requêtes"
        assert success_rate > 98, "Taux de succes "
    
    # Assertions pour les requêtes moyennes (nb = 100)
    elif nb == 100:
        assert average_response_time < 0.5, f"Temps de réponse moyen élevé: {average_response_time} secondes pour {nb} requêtes"
        assert success_rate > 98, "Taux de succes"


    elif nb == 1000:
        assert average_response_time < 1.0, f"Temps de réponse moyen élevé: {average_response_time} secondes pour {nb} requêtes"
        assert success_rate > 95, "Taux de succes"
        

    # Assertion générale pour le taux de succès
    # assert success_rate >= 90, "Le taux de succès est inférieur à 90%"
    
    
    
@pytest.mark.parametrize('nb', [10, 100, 1000] )
def test_postperf(nb):
    for id in range(1):  # Répétez le test 5 fois pour chaque valeur de nb
        run(nb)
        
        

if __name__ == "__main__":
    pytest.main()




