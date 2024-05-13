import requests
from Api.changerequest.pict import BASE_URL , AUTHORIZATION_TOKEN


class Apichangerequest:
   
   
    def __init__(self):
       
        self.base_url = BASE_URL
        
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': AUTHORIZATION_TOKEN
        }
         
         
        self.idput =   "7ad17c47-c2bd-45b0-bbba-1c1dec0379ab"
        
        
        self.idelete = "3e3f768d-82d3-4bea-a244-4a1dea04d5d1"
         
        self.state = "Filters=state == 0"
      
        self.paramsearch = "SortOrder = -startDate&PageNumber=1&Filters=state == 0&PageSize=1"
         
       
         
    def post_changerequest(self,data):
        
        url = BASE_URL
        print("URL utilisée :", url)
        response = requests.post(url,json=data , headers=self.headers , verify=False)
        
        return response
    
    
    
    def put_changerequest(self,data):
        
        url = f"{BASE_URL}/{self.idput}"
        
        print("URL utilisée :", url)
        
        response = requests.put(url,  json=data , headers=self.headers , verify=False )
        
        return response



    
    def delete_changerequest(self):
        
        url =  f"{BASE_URL}/{self.idelete}"
        print("URL utilisée :", url)
        response = requests.delete(url, headers=self.headers , verify=False )
        
        return response
    
    
    
    def get_listchangerequest(self):
        
        url =  f"{BASE_URL}?{self.state}"
        print("URL utilisée :", url)
        response = requests.get(url, headers=self.headers , verify=False, params=self.state)
        
        return response
        
    

    def get_searchangerequest(self):
        
        url =  f"{BASE_URL}?{self.paramsearch}"
        print("URL utilisée :", url)
        response = requests.get(url, headers=self.headers , verify=False, params=self.paramsearch)
        
        return response 