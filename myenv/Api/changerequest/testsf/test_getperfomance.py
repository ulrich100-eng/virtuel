import pytest
import requests
import concurrent.futures
import random
import time
import multiprocessing
# from Api.changerequest.testsf.api_change import Apichange

API_URL = "http://localhost:3000/hello"  # Remplacez ceci par l'URL de votre API




# def api_change():
#     return Apichange()


@pytest.mark.parametrize("num_requests", [9, 100, 1000])
@pytest.mark.performance
def test_api_performance(num_requests):
    if num_requests == 9:
        normal_load_scenario()
    # elif num_requests == 100:
    #     high_load_scenario()
    # elif num_requests == 1000:
    #     max_load_scenario()


def send_request():
    start_time = time.time()
    response = requests.get(API_URL)
    end_time = time.time()
    response_time = end_time - start_time
    print("Temps  d'exécution d'une requete:", response_time)
    is_success = response.status_code == 200
    return response_time, is_success

def normal_load_scenario():
    success_count = 0
    total_time = 0
    failure_count = 0 
    throughput = 0
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(send_request) for _ in range(9)]

        for future in concurrent.futures.as_completed(futures):
            response_time, is_success = future.result()
            total_time += response_time
            print("Temps total  d'exécution :", total_time)
            if is_success:
                success_count += 1
              
            else:
                failure_count += 1
                
     # Calcul du temps de réponse moyen
    average_response_time = total_time / 9
    print(f"Temps de réponse moyen : {average_response_time} secondes")
    
    # Calcul du débit (requêtes par seconde)
    throughput = success_count / total_time  
    print(f"Le debit : {throughput}")
     
      # Calcul du taux de succès et d'échec
    
    success_rate = (success_count / 10) * 100
    
    print(f"Taux de succès : {success_rate}%")
    
    
    failure_rate = (failure_count / 10) * 100
    print(f"Taux d'échec : {failure_rate}%")
     
    assert success_count == 9, "Not all requests succeeded"
    assert average_response_time < 1, f"Average response time exceeded 1 second: {average_response_time} seconds"


# def high_load_scenario():
#     success_count = 0

#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         futures = [executor.submit(send_request) for _ in range(100)]

#         for future in concurrent.futures.as_completed(futures):
#             _, is_success = future.result()
#             if is_success:
#                 success_count += 1

#     assert success_count == 100, "Not all requests succeeded"

# def max_load_scenario():
#     success_count = 0
#     failure_count = 0

#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         futures = [executor.submit(send_request) for _ in range(1000)]

#         for future in concurrent.futures.as_completed(futures):
#             _, is_success = future.result()
#             if is_success:
#                 success_count += 1
#             else:
#                 failure_count += 1

#     assert failure_count == 0, "Some requests failed"
#     assert success_count >= 900, "Not enough successful requests"

# @pytest.mark.performance
# def test_long_duration_scenario():
#     start_time = time.time()
#     end_time = start_time + 3600  # 1 heure

#     success_count = 0
#     failure_count = 0

#     while time.time() < end_time:
#         response_time, is_success = send_request()
#         if is_success:
#             success_count += 1
#         else:
#             failure_count += 1

#     total_requests = success_count + failure_count
#     assert failure_count / total_requests < 0.1, "Failure rate too high"
#     assert success_count > 0, "No successful requests made"

#     average_response_time = (end_time - start_time) / total_requests
#     assert average_response_time < 1, f"Average response time exceeded 1 second: {average_response_time} seconds"
