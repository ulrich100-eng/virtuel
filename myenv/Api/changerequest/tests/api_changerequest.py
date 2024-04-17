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
         
        self.params = {
            "PageNumber": 2,
            "PageSize": 2,
            "SortOrder": "-startDate",
            "Filters": "state==0"
        }
        
         
    def post_changerequest(self,data):
        
        url = BASE_URL
    
        response = requests.post(url,   json=data ,  headers=self.headers , verify=False)
        
        return response
    
    
    
    def put_changerequest(self,data):
        
        url = f"{BASE_URL}/14b7d651-eddd-40f5-a122-ab51d660e874"
        
        response = requests.put(url, json=data , headers=self.headers , verify=False )
        
        return response



    
    def delete_changerequest(self):
        
        url =  f"{BASE_URL}/1742be55-09a8-4d1c-8550-bd1de152f686"
        
        response = requests.delete(url, headers=self.headers , verify=False )
        
        return response
    
    
    
    def get_changerequest(self):
        
        url =  f"{BASE_URL}/{self.params}"
        print(f"Sending GET request to URL: {url}")
        
        response = requests.get(url, headers=self.headers , verify=False, params=self.params )
        
        return response
        