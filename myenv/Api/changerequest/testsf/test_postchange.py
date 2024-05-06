import pytest
import requests
import time
import pytest_benchmark
# URL de l'API et jeton d'accès
API_URL = "https://change-request.perfit.apps.dev.orange.local/api/changerequests"
BEARER_TOKEN = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJrSnRxNGNzNkRJRllNZFJ0TFMzeE5EcTNFN0M3UzBnWlVOeUZMQmYwZjVVIn0.eyJleHAiOjE3MTQ4MzA5MTQsImlhdCI6MTcxNDgzMDAxNCwiYXV0aF90aW1lIjoxNzE0ODMwMDEyLCJqdGkiOiI5ZmQyNGNlYS1kYjMxLTRiY2MtYWExOS1jNTU3YWFkNTEwMTAiLCJpc3MiOiJodHRwczovL2tleWNsb2FrLXByZXByb2QuYXBwcy5kZXYub3JhbmdlLmxvY2FsL3JlYWxtcy9kaWdpdGFsLWFwcCIsImF1ZCI6InBlcmZpdCIsInN1YiI6IjA0OWU0YjUxLWVhNWUtNDMxYy04ZTEwLTJlZmQ3OWE4YWIxMiIsInR5cCI6IklEIiwiYXpwIjoicGVyZml0Iiwibm9uY2UiOiI5MDlkYzEzNS1kZmFhLTRmYmMtOWM2Zi1jZWYyZjIwZDhiOTMiLCJzZXNzaW9uX3N0YXRlIjoiZjIwNGI1ZjgtNjc4ZS00MzNmLWEwYzctZWNmMmQ3NmU1NzZhIiwiYXRfaGFzaCI6IkQwdWJSZHl3bHhIbjJNM1NSeUdmUEEiLCJzaWQiOiJmMjA0YjVmOC02NzhlLTQzM2YtYTBjNy1lY2YyZDc2ZTU3NmEiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJLRU5HTkUgIEtFTkdORSIsInByZWZlcnJlZF91c2VybmFtZSI6InpiaHE4MzQ5IiwiZ2l2ZW5fbmFtZSI6IktFTkdORSAiLCJmYW1pbHlfbmFtZSI6IktFTkdORSIsImVtYWlsIjoidWxyaWNoLmtlbmduZUBvcmFuZ2UuY29tIn0.dg6vO182hnizSIKucI-TZqCyQj6nmaOFcW--5huXrcEsctXWo24ektvX_kY0p6kjnD_FKqVwZ3NysMkZ79Y7tociq2l7HocLY6ErkF76FiZfXkzCvMf0l6_bXWkV0fiGsyjukCF429Y9VoOIQOZ6X5a55gT9eyMuwVXmpytlcAWXWYn9pCaBOpSKeRo7uI_lzf2wjikK8oHnlrNkcOq7Wyn5VH7hGE2DMpXLJpnrDgFvxq58Iu_gncDxhd6ngNiP-AFC2gN6JZkGUtrXRMQ8ZfjkgzkgWI29L0R2k-Kqe8yzjbBzhiVu9fewKrPQ8v6cI_woV6KiHjOy3xbDI7YGjg"

# Fonction pour envoyer une requête POST avec les données fournies
def send_post_request(url, headers, data):
    response = requests.post(url, headers=headers, json=data, verify=False)
    return response






# Test de performance pour la fonctionnalité d'API POST
@pytest.mark.performance
def test_api_post_performance():
    # URL de l'utilisateur
    user_url = "https://change-request.perfit.apps.dev.orange.local/api/changerequests"

    # Corps de la requête
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

    # En-têtes de la requête avec le jeton d'accès
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }

    # Nombre de requêtes à envoyer pour le test de performance
    num_requests = 100
 

    # Envoi de plusieurs requêtes et mesure du temps d'exécution total
    for _ in range(num_requests):
        start_time = time.time()
        response = send_post_request(user_url, headers, request_body)
        assert response.status_code == 401
        end_time = time.time()
        total_time += end_time - start_time

    # Calcul de la moyenne du temps d'exécution par requête
    average_time = total_time / num_requests

    # Assertion pour vérifier si la moyenne du temps est inférieure à 1 seconde
    assert average_time < 1, f"Average time exceeded 1 second: {average_time} seconds"
