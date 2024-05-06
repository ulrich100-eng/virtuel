import pytest
import requests
import time

@pytest.mark.performance
def test_response_time():
    start_time = time.time()  # Temps de départ

    response = requests.get("http://localhost:3000/hello")

    end_time = time.time()  # Temps d'arrivée
    elapsed_time = end_time - start_time  # Temps écoulé
    print(f"Elapsed time: {elapsed_time} seconds")
    assert response.status_code == 200
    assert elapsed_time < 1.0  # Vérifie si le temps de réponse est inférieur à 1 seconde

