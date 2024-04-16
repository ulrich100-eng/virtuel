import requests
from config import BASE_URL , AUTHORIZATION_TOKEN 


class Apichangerequest:
   
   
    def __init__(self):
       
        self.base_url = BASE_URL
        
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': AUTHORIZATION_TOKEN
        }
         
         
         
    def post_changerequest(self,data):
        
        url = BASE_URL
    
        response = requests.post(url,   json=data ,  headers=self.headers , verify=False)
        
        return response

  
