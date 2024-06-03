import requests
from Api.pict import  AUTHORIZATION_TOKEN_WORKPACKAGE , BASE_URL_WORK



class Apiworkpackage:
    
    
    def __init__(self):
       
        
        self.base = BASE_URL_WORK
        
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': AUTHORIZATION_TOKEN_WORKPACKAGE
        }
        
        self.idpostworkpackage =  "ChangeRequestId=6c7dda77-9f8e-4729-b5f2-c3acdeb0add3"
        
        self.idgetworkpackage = "Type=0"
        
        self.idgetworkpackageassign = "Type=0&Assignee==mhdl5011"
     
        self.idgetworkpackageinput = "Type=0&Assignee==mhdl5011&Input=monprojet"
     
     
     
     
     
     
    def post_workpackage(self,data):
        
      
        url = f"{BASE_URL_WORK}?{self.idpostworkpackage}"
        print("URL utilisée :", url)
        response = requests.post(url,json=data , headers=self.headers , verify=False)
        
        return response
    
    
    
    
    def get_workpackage(self):
        
      
        url = f"{BASE_URL_WORK}?{self.idgetworkpackage}"
        print("URL utilisée :", url)
        
        response = requests.get(url , headers=self.headers , verify=False)
        
        return response
    
    
    
    def get_workpackageassigndemand(self):
        
        
        url = f"{BASE_URL_WORK}?{self.idgetworkpackageassign}"
        
        print("URL utilisée :", url)
        
        response = requests.get(url,  headers=self.headers , verify=False )
        
        return response
    
    
    
    
    
    def get_workpackageinput(self):
        
        
        url = f"{BASE_URL_WORK}?{self.idgetworkpackageinput}"
        
        print("URL utilisée :", url)
        
        response = requests.get(url,  headers=self.headers , verify=False )
        
        return response
    
    
    
    
   