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
    
    
    def put_changerequest(self,data,put_id):
        
        url = f"{BASE_URL}/{put_id}"
        
        response = requests.put(url, json=data , headers=self.headers , verify=False )
        
        return response

    
    def delete_changerequest(self,request_id):
        
        url =  f"{BASE_URL}/{request_id}"
        
        response = requests.delete(url, headers=self.headers , verify=False )
        
        return response