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
         
        self.paramslist = {
            "PageNumber": 0,
            "PageSize": 0,
            "SortOrder": "",
            "Filters": "state==0"
        }
        
        self.paramsrech = {
            "PageNumber": 0,
            "PageSize": 0,
            "SortOrder": "",
            "Filters": "state==0"
        }
         
    def post_changerequest(self,data):
        
        url = BASE_URL
    
        response = requests.post(url,   json=data ,  headers=self.headers , verify=False)
        
        return response
    
    
    
    def put_changerequest(self,data):
        
        url = f"{BASE_URL}/d469f318-a79c-4806-ab8d-e9baf0ec2fd6"
        
        print("URL utilisée :", url)
        
        response = requests.put(url, json=data , headers=self.headers , verify=False )
        
        return response



    
    def delete_changerequest(self):
        
        url =  f"{BASE_URL}/a77c75b1-17fb-4bfc-ad5c-d6fa8359e41e"
     
        response = requests.delete(url, headers=self.headers , verify=False )
        
        return response
    
    
    
    def get_listchangerequest(self,paramslist):
        
        url =  f"{BASE_URL}?{self.paramslist}"
        print("URL utilisée :", url)
        response = requests.get(url, headers=self.headers , verify=False, params=paramslist)
        
        return response
        
    
    
    def get_rechchangerequest(self,parameters):
        
        url =  f"{BASE_URL}?{self.paramsrech}"
     
        response = requests.get(url, headers=self.headers , verify=False, params=parameters )
        
        return response