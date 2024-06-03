import requests
# from urllib.parse import urlparse
import json
from urllib.parse import urlparse, urlencode, parse_qs , urlunparse
import urllib.parse





class Apichangeperf:
    
    
    base = "https://change-request.perfit.apps.dev.orange.local"
    
    pochange = "/api/changerequests"
    puchange = "/api/changerequests/7ad17c47-c2bd-45b0-bbba-1c1dec0379ab"
    delchange = "/api/changerequests/7ad17c47-c2bd-45b0-bbba-1c1dec0379ab"
    idputclose = "/close?id=f1d4a97b-344b-41f7-b9af-beffb23ca302"
    headers = {
        'content-type': 'application/json',
    }
    
    token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJrSnRxNGNzNkRJRllNZFJ0TFMzeE5EcTNFN0M3UzBnWlVOeUZMQmYwZjVVIn0.eyJleHAiOjE3MTY4Mjg1MjgsImlhdCI6MTcxNjgyNzYyOCwiYXV0aF90aW1lIjoxNzE2ODI3NjI3LCJqdGkiOiI3ZWU3YWY4Ny04MTdlLTQxNzctOGIwYS1hODcwNGQxZmY3NzgiLCJpc3MiOiJodHRwczovL2tleWNsb2FrLXByZXByb2QuYXBwcy5kZXYub3JhbmdlLmxvY2FsL3JlYWxtcy9kaWdpdGFsLWFwcCIsImF1ZCI6InBlcmZpdCIsInN1YiI6IjA0OWU0YjUxLWVhNWUtNDMxYy04ZTEwLTJlZmQ3OWE4YWIxMiIsInR5cCI6IklEIiwiYXpwIjoicGVyZml0Iiwibm9uY2UiOiIxNTRmYTU5YS0wZjU1LTRiM2UtYTAzMS1lNDUwMDg4MmViNmYiLCJzZXNzaW9uX3N0YXRlIjoiOTY2YjVlMjQtNjk3OS00MTdiLWE2MjEtMWViOTlmMDliZjAzIiwiYXRfaGFzaCI6ImkzU3h5QVo1Q2lLSmdnZ2E2aXdaRmciLCJzaWQiOiI5NjZiNWUyNC02OTc5LTQxN2ItYTYyMS0xZWI5OWYwOWJmMDMiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJLRU5HTkUgIEtFTkdORSIsInByZWZlcnJlZF91c2VybmFtZSI6InpiaHE4MzQ5IiwiZ2l2ZW5fbmFtZSI6IktFTkdORSAiLCJmYW1pbHlfbmFtZSI6IktFTkdORSIsImVtYWlsIjoidWxyaWNoLmtlbmduZUBvcmFuZ2UuY29tIn0.DafAE23oqauEeQTv3FoAgNhKQKzPghg18YagET1_0ihn3eiaKqUjL4mthHVxdUfp_pPCDur11SQjLXzLd6iGxT8O6NhBesgy2bLjxHhry2MRSG4-ofP7lXiBkBt4qB3aHg83P9_V_S3mGAyYABh5cnHKAqfWxzRoRtAB7v5WSA8dg0vPQn_maZEU7m4Mt_RFKEd-op6aVq92pIUTg1VTJB73otksXKSQOPgsQMUBmeqoNAa7PERgmGP8Q0CdVOCdEk_zkWcF5V-hDIdhXGJzix5mWIPMI9boqrUhON02Q0E2SP9CPKMXL1F5_FzvIpu-R70hAJ_hr1_oT4-9qUehfA'
    
    tokenworkpackage = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJrSnRxNGNzNkRJRllNZFJ0TFMzeE5EcTNFN0M3UzBnWlVOeUZMQmYwZjVVIn0.eyJleHAiOjE3MTcwODMyOTMsImlhdCI6MTcxNzA4MjM5MywiYXV0aF90aW1lIjoxNzE3MDgyMzc3LCJqdGkiOiIwZDBlY2MzYi1lYWMxLTRhNTYtYjJiOS1lNWU5NzRmNzQ4NGQiLCJpc3MiOiJodHRwczovL2tleWNsb2FrLXByZXByb2QuYXBwcy5kZXYub3JhbmdlLmxvY2FsL3JlYWxtcy9kaWdpdGFsLWFwcCIsInN1YiI6IjA0OWU0YjUxLWVhNWUtNDMxYy04ZTEwLTJlZmQ3OWE4YWIxMiIsInR5cCI6IkJlYXJlciIsImF6cCI6InBlcmZpdCIsIm5vbmNlIjoiMTQxOWIzZTgtMTBhMy00Y2FjLTg2NTUtYmVjNWViYWNiMzE5Iiwic2Vzc2lvbl9zdGF0ZSI6ImJjNjgzZTM1LWQ0MTQtNGYxNS05YTczLTllYjIxZDQyNjdkZSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInJlc291cmNlX2FjY2VzcyI6eyJwZXJmaXQiOnsicm9sZXMiOlsiUmVhZFByZWZlcmVuY2UiLCJVcGRhdGVQcm9qZWN0V29ya3BhY2thZ2UiLCJTeW5jT3BlblByb2plY3QiLCJSZWFkUmlzayIsIkRlbGV0ZVByb2plY3RDdXN0b21GaWVsZCIsIlJlYWRUeXBlUHJvamVjdEN1c3RvbUZpZWxkIiwiVXBkYXRlUHJvamVjdFBlcm1pc3Npb25UeXBlIiwiQ3JlYXRlUHJlZmVyZW5jZSIsIkNyZWF0ZVByb2plY3RQZXJtaXNzaW9uVHlwZSIsIlJlYWRQcm9qZWN0V29ya3BhY2thZ2UiLCJDcmVhdGVBZHZpY2UiLCJBc3NpZ25DaGFuZ2VSZXF1ZXN0QkkiLCJSZWFkQWxlcnRlIiwiUmVhZEltcGFjdCIsIlVwZGF0ZVByb2plY3RQZXJtaXNzaW9uIiwiRGVsZXRlUHJvamVjdERlY2lzaW9uIiwiQ3JlYXRlTWVtYmVyIiwiUmVhZFByb2plY3RNZW1iZXIiLCJDcmVhdGVQcm9qZWN0UGVybWlzc2lvblVzZXIiLCJEZWxldGVQcm9qZWN0UGVybWlzc2lvblR5cGUiLCJEZWxldGVQcmVmZXJlbmNlIiwiUmVhZFByb2plY3REZWNpc2lvbiIsIlJlYWRQcm9qZWN0UGVybWlzc2lvblR5cGUiLCJDcmVhdGVUeXBlUHJvamVjdEN1c3RvbUZpZWxkIiwiQ3JlYXRlUHJvamVjdE1lbWJlciIsIlJlYWRBZHZpY2UiLCJDcmVhdGVDaGFuZ2VSZXF1ZXN0RFJTIiwiUmVhZFByb2plY3RDdXN0b21GaWVsZCIsIkRlbGV0ZVByb2plY3RQZXJtaXNzaW9uVXNlciIsIkNyZWF0ZVByb2plY3RXb3JrcGFja2FnZSIsIlJlYWREZW1hbmRlIiwiRGVsZXRlUHJvamVjdE1lbWJlciIsIkltcG9ydFByb2plY3RzIiwiUmVhZE9wZW5Qcm9qZWN0U3RhdHVzZSIsIlJlYWRDaGFuZ2VSZXF1ZXN0RFJTIiwiRGVsZXRlUHJvamVjdFBlcm1pc3Npb24iLCJSZWFkUHJvamVjdFBlcm1pc3Npb25Vc2VyIiwiRGVsZXRlUHJvamVjdCIsIlVwZGF0ZVByb2plY3REZWNpc2lvbiIsIlVwZGF0ZURlY2lzaW9uIiwiQ3JlYXRlUHJvamVjdEN1c3RvbUZpZWxkIiwiVXBkYXRlRGVtYW5kZSIsIkNIRUZfREVQQVJURU1FTlQiLCJEZWxldGVQcm9qZWN0V29ya3BhY2thZ2UiLCJVcGRhdGVBbGVydGUiLCJSZWFkUHJvamVjdEtwaXMiLCJDcmVhdGVEZW1hbmRlIiwiVXBkYXRlSW1wYWN0IiwiQXNzaWduQ2hhbmdlUmVxdWVzdERSUyIsIkRlbGV0ZVJpc2siLCJEZWxldGVBZHZpY2UiLCJDaGVmUHJvamV0IiwiVXBkYXRlVHlwZVByb2plY3RDdXN0b21GaWVsZCIsImFkbWluIiwiQ3JlYXRlUHJvamVjdCIsIlJlYWRlckRlbWFuZGUiLCJEZWxldGVEZW1hbmRlIiwiUmVhZFByb2plY3RQZXJtaXNzaW9uIiwiVGVhbV9NZW1iZXIiLCJHVV9BZG1pbiIsIkNyZWF0ZVByb2plY3REZWNpc2lvbiIsIkJ1aXNpbmVzc19NYW5hZ2VyIiwiQ3JlYXRlQ2hhbmdlUmVxdWVzdEJJIiwiQ3JlYXRlQWxlcnRlIiwiQ3JlYXRlSW1wYWN0IiwiQ3JlYXRlRGVjaXNpb24iLCJEZWxldGVBbGVydGUiLCJSZWFkUHJvamVjdCIsIkRlbGV0ZURlY2lzaW9uIiwiQ3JlYXRlUmlzayIsIlVwZGF0ZUFkdmljZSIsIlJlYWRQcmlvcml0eSIsIkNIRUZfU0VSVklDRSIsIlJlYWREZWNpc2lvbiIsIlVwZGF0ZVByb2plY3RDdXN0b21GaWVsZCIsIlBNTyIsIlVwZGF0ZVByb2plY3QiLCJVcGRhdGVQcm9qZWN0UGVybWlzc2lvblVzZXIiLCJVcGRhdGVSaXNrIiwiUmVhZE9wZW5Qcm9qZWN0Um9sZXMiLCJSZWFkQ2hhbmdlUmVxdWVzdEJJIiwiRGVsZXRlSW1wYWN0IiwiQ3JlYXRlUHJvamVjdFBlcm1pc3Npb24iLCJEZWxldGVUeXBlUHJvamVjdEN1c3RvbUZpZWxkIiwiUmVhZFByb2plY3RXb3JrcGFja2FnZUFjdGl2aXRpZXMiXX19LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwic2lkIjoiYmM2ODNlMzUtZDQxNC00ZjE1LTlhNzMtOWViMjFkNDI2N2RlIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJuYW1lIjoiS0VOR05FICBLRU5HTkUiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ6YmhxODM0OSIsImdpdmVuX25hbWUiOiJLRU5HTkUgIiwiZmFtaWx5X25hbWUiOiJLRU5HTkUiLCJlbWFpbCI6InVscmljaC5rZW5nbmVAb3JhbmdlLmNvbSJ9.dW4mgYHuymMvEEaqIV8kA53pHOc8gKOFIVQW2O29BGFwY1xiFD0oBN3TQh9tbyGYzww2BNRF3PLmgehNYGyvKhH6Y8aNj9N5YtHuO1Dv6kbtIOw56am2U0dfh8YlRmjhOzmqU3wK4JZ3bAke4RpNJU1KycdFofJkFCOPP2rz-iFo71Hzf0gYmj2hN9Va5BAKEWs30CXJG32UmgNSDbw53CR__rBjbidA2K-g79FNv9tBP4aa-Efc415ngoYz4ElupWAMQdXV0OJrdQ2hq7MB3kk1etyusbhce_uEhvKcK-ToM2wxs9Wa8fVMQYQueIdZstCkTCCoRqP7jZs7a03B7g'
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
        # print("URL utilisée :", sanitized_url)
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
   



    def put_closeperf(self):
        
    
          header = self.headers.copy()
          header['Authorization'] = self.tokenworkpackage
          response = requests.request('PUT', self.base+self.pochange+self.idputclose, headers=header, verify=False, timeout=30)
          return response
    
    
# if __name__=='__main__':
    #   p = Apichange()
   
    
    #   for i in range(2):
        #  p.post_changeperf()
        # p.put_changeperf()
          # p.get_changeperflist()
         #  p.get_changeperfsearch()
            
        
    
    