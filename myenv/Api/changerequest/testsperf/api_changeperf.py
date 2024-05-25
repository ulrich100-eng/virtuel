import requests
# from urllib.parse import urlparse
import json
from urllib.parse import urlparse, urlencode, parse_qs , urlunparse
import urllib.parse





class Apichange:
    
    
    base = "https://change-request.perfit.apps.dev.orange.local"
    
    pochange = "/api/changerequests"
    puchange = "/api/changerequests/7ad17c47-c2bd-45b0-bbba-1c1dec0379ab"
    delchange = "/api/changerequests/7ad17c47-c2bd-45b0-bbba-1c1dec0379ab"
    
    headers = {
        'content-type': 'application/json',
    }
    
    token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJrSnRxNGNzNkRJRllNZFJ0TFMzeE5EcTNFN0M3UzBnWlVOeUZMQmYwZjVVIn0.eyJleHAiOjE3MTY2NDI1MTUsImlhdCI6MTcxNjY0MTYxNSwiYXV0aF90aW1lIjoxNzE2NjQxNjEyLCJqdGkiOiI1YjFhOTJkZS01MjJiLTRmZTUtOWI2Mi04MTU4ZDY1MTBkNDQiLCJpc3MiOiJodHRwczovL2tleWNsb2FrLXByZXByb2QuYXBwcy5kZXYub3JhbmdlLmxvY2FsL3JlYWxtcy9kaWdpdGFsLWFwcCIsImF1ZCI6InBlcmZpdCIsInN1YiI6IjA0OWU0YjUxLWVhNWUtNDMxYy04ZTEwLTJlZmQ3OWE4YWIxMiIsInR5cCI6IklEIiwiYXpwIjoicGVyZml0Iiwibm9uY2UiOiJjMTQ3NDk3My1mNzBjLTRmZWQtODAyYi04ZTMyNWM5YWIzMTUiLCJzZXNzaW9uX3N0YXRlIjoiMjU3YjVlMDItNzNjMC00OGZmLWIwN2UtOGUzZWJjOWRkZWYzIiwiYXRfaGFzaCI6Ik1QRTd4RmxqU0RlenI1ZkQ5U2xBRUEiLCJzaWQiOiIyNTdiNWUwMi03M2MwLTQ4ZmYtYjA3ZS04ZTNlYmM5ZGRlZjMiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJLRU5HTkUgIEtFTkdORSIsInByZWZlcnJlZF91c2VybmFtZSI6InpiaHE4MzQ5IiwiZ2l2ZW5fbmFtZSI6IktFTkdORSAiLCJmYW1pbHlfbmFtZSI6IktFTkdORSIsImVtYWlsIjoidWxyaWNoLmtlbmduZUBvcmFuZ2UuY29tIn0.ALwH81cZXwPNZzLDKmFKoWh4gwEeHGbI7sKvmvGGbBL2nbXFLWD7xV-ztlqZkxh9gXVjl8l2rboS6XnDV0ePi1oKRJLZN6pL7aDZIEQiPF73yGFyS1V83Xg4zHR8o2UMZ4efSfGIfGNQnbDZgXXCWlcSRUZeH_kMxoR918QWlA-vasUhdmnzV65YWKKbO_oH3yJcLgOUCjkMtf3OSn-3KC_osRQ1GRcQ0BfNfoNVjEAp-82USn4JhKohiczogQIANEabMxeaNtXE6EuvRku8BV0s62bZTEtowkk7wVgfwQQuXLTIztX9sPdMhejaTW_AN3LcYvLMixeZrJKojxYIVg'
    
    
    # def __init__(self) -> None:
    #         self.token_a_to_invalidate = ''


    def sanitize_url(self, url):
        
        # Parse l'URL pour extraire les composants, notamment les paramètres de requête
        parsed_url = urlparse(url)
        
        # Extraire les paramètres de requête sous forme de dictionnaire
        query_params = parse_qs(parsed_url.query)
        
        # Nettoyer le paramètre 'Filters'
        filters_value = query_params['Filters'][0]
        # Nettoyer la valeur des filtres, par exemple en remplaçant les espaces et les égalités
        sanitized_filters_value = filters_value.replace(' ', '%20').replace('==', '%3D%3D')
        # Mettre à jour la valeur des filtres dans les paramètres de requête
        query_params['Filters'] = sanitized_filters_value
        
         # Reconstruire la chaîne de requête avec les paramètres nettoyés
        sanitized_query = urlencode(query_params, doseq=True)
        
        # Reconstruire l'URL complète avec la chaîne de requête nettoyée
        sanitized_url = urlunparse(parsed_url._replace(query=sanitized_query))
        
        return sanitized_url
        
        

    def check_status(self, status_code):
        result = False
        if status_code // 100 == 2:
            print("Success! Status Code:", status_code)
            result = True
        elif status_code // 100 == 4:
            print("Client Error! Status Code:", status_code)
            result = False
        elif status_code // 100 == 5:
            print("Server Error! Status Code:", status_code)
            result = False
        else:
            print("Unexpected Status Code:", status_code)
            result = False
        
        assert result, f"We did not get a successful response from the server, so this test instance failed. Status Code: {status_code}"
        return result




    def post_changeperf(self, data):
        
        
        header = self.headers.copy()
        header['Authorization'] = self.token
        response = requests.request('POST', self.base+self.pochange, json=data, headers=header, verify=False, timeout=30)
        return response
    
    
    
    def put_changeperf(self, data):
        
    
        header = self.headers.copy()
        header['Authorization'] = self.token
        response = requests.request('PUT', self.base+self.puchange, json=data, headers=header, verify=False, timeout=30)
        return response
    
    
    
       
    def get_changeperflist(self):
        
    
        header = self.headers.copy()
        header['Authorization'] = self.token
        
        # Construire l'URL avec les filtres
        url = f"{self.base}{self.pochange}?Filters=state == 0"
        
        # Nettoyer l'URL
        sanitized_url = self.sanitize_url(url)
        response = requests.request('GET', sanitized_url, headers=header, verify=False, timeout=30)
        return response
    
    
    
    
    def get_changeperfsearch(self):
        
    
        header = self.headers.copy()
        header['Authorization'] = self.token
        
        # Construire l'URL avec les filtres
        url = f"{self.base}{self.pochange}?SortOrder = -startDate&PageNumber=1&Filters=state == 0&PageSize=1"
        
        # Nettoyer l'URL
        sanitized_url = self.sanitize_url(url)
        response = requests.request('GET', sanitized_url, headers=header, verify=False, timeout=30)
        return response
    
    
      
    def delete_changeperf(self):
        
    
        header = self.headers.copy()
        header['Authorization'] = self.token
        response = requests.request('DELETE', self.base+self.delchange, headers=header, verify=False, timeout=30)
        return response
   

# if __name__=='__main__':
    #   p = Apichange()
   
    
    #   for i in range(2):
        #  p.post_changeperf()
        # p.put_changeperf()
          # p.get_changeperflist()
         #  p.get_changeperfsearch()
            
        
    
    