import requests
from Api.pict import BASE_URL , AUTHORIZATION_TOKEN , AUTHORIZATION_TOKEN_WORKPACKAGE
from urllib.parse import urlparse, urlencode, parse_qs , urlunparse 

class Apichangerequest:
   
   
    def __init__(self):
       
        self.base_url = BASE_URL
        
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': AUTHORIZATION_TOKEN
        }
         
         
        self.headers1 = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': AUTHORIZATION_TOKEN_WORKPACKAGE
        }
       
         
        self.idput =   "7ad17c47-c2bd-45b0-bbba-1c1dec0379ab"
        
        self.idputclose = "close?id=f1d4a97b-344b-41f7-b9af-beffb23ca302"
        
        self.idelete = "3e3f768d-82d3-4bea-a244-4a1dea04d5d1"
         
        self.paramsearch = "SortOrder = -startDate&PageNumber=1&Filters=state == 0&PageSize=1"
        
        self.state = "Filters=state == 0"
         
       
       
       
       
         
    def post_changerequest(self,data):
        
        url = BASE_URL
        print("URL utilisée :", url)
        response = requests.post(url,json=data , headers=self.headers , verify=False)
        
        return response
    
    
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
        print("URL utilisée :", sanitized_url)
        return sanitized_url
   
        
    
    def put_changerequest(self,data):
        
        url = f"{BASE_URL}/{self.idput}"
        
        print("URL utilisée :", url)
        
        response = requests.put(url,  json=data , headers=self.headers , verify=False )
        
        return response



    
    def delete_changerequest(self):
        
        url =  f"{BASE_URL}/{self.idelete}"
        print("URL utilisée :", url)
        response = requests.delete(url, headers=self.headers    , verify=False )
        
        return response
    
    
    
    def get_listchangerequest(self):
        # Construire l'URL avec les filtres
        url = f"{BASE_URL}?{self.state}"
        
        # Nettoyer l'URL
        sanitized_url = self.sanitize_url(url)
        
        print("URL utilisée :", url)
        
        response = requests.get(sanitized_url, headers=self.headers, verify=False)
        
        return response
    


    def get_searchangerequest(self):
        
        
        url =  f"{BASE_URL}?{self.paramsearch}"
        
        print("URL utilisée :", url)
        
        response = requests.get(url, headers=self.headers , verify=False)
        
        return response 
    
    
    
    
    
    def put_changerequestclose(self):
        
      
        url = f"{BASE_URL}/{self.idputclose}"
        
        print("URL utilisée :", url)
        
        response = requests.put(url,  headers=self.headers1 , verify=False )
        
        return response
    
    
    
    
    def get_changerequestinput(self):
        
        
        url = f"{BASE_URL}={self.idputclose}"
        
        print("URL utilisée :", url)
        
        response = requests.get(url,  headers=self.headers , verify=False )
        
        return response
       

    
    
    
    