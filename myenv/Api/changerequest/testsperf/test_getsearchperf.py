import pytest
import time
import concurrent.futures  
from Api.changerequest.testsperf.api_changeperf import Apichange  # Assurez-vous que le chemin est correct





def getsearch(nb):
    
    api_change = Apichange()
    
    print(f"Received nb: {nb}")
    
    failure_count = 0 
    success_count = 0
    
    start_time = time.time()
    print(f"Running test with {nb} requests")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=nb) as executor:
        results = list(executor.map(lambda _: api_change.get_changeperfsearch(), range(nb)))
    
    end_time = time.time()

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


    elif nb == 500:
            assert average_response_time < 0.5, f"Temps de réponse moyen élevé: {average_response_time} secondes pour {nb} requêtes"
            assert success_rate > 98, "Taux de succes"


    elif nb == 1000:
        assert average_response_time < 1.0, f"Temps de réponse moyen élevé: {average_response_time} secondes pour {nb} requêtes"
        assert success_rate > 95, "Taux de succes"
        

    # Assertion générale pour le taux de succès
    # assert success_rate >= 90, "Le taux de succès est inférieur à 90%"
    
    
    
@pytest.mark.parametrize('nb', [10, 100, 500 ,10] )
def test_getperfsearch(nb):
    for id in range(1):  # Répétez le test 1 foi pour chaque valeur de nb
        getsearch(nb)
        
        

if __name__ == "__main__":
    pytest.main()




