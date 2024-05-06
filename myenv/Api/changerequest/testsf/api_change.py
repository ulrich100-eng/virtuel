# import requests
# from Api.changerequest.pict import BASE_URL , AUTHORIZATION_TOKEN


# class Apichange:
   
   
#     def __init__(self):
       
#         self.base_url = BASE_URL
        
#         self.headers = {
#             'Accept': 'application/json',
#             'Content-Type': 'application/json',
#             'Authorization': AUTHORIZATION_TOKEN
#         }
         
         
#         # self.idput =   "23074633-2087-40af-8d7e-7af69576a62e"
        
        
#         # self.idelete = "cd938521-38ef-44fa-bb02-d613c71455a5"
         
         
#         # self.paramslist = {
            
#         #     'Filters': 'state==0'
#         # }
        
        
#         # self.paramsearch = {
#         #     'PageNumber': 2,
#         #     'PageSize': 2,
#         #     'SortOrder': 'SortOrder = -startDate',
#         #     'Filters': 'state==0'
#         # }
         
         
         
    # def post_change(self,data):
        
    #     url = BASE_URL
    #     print("URL utilisée :", url)
    #     response = requests.post(url,   json=data ,  headers=self.headers , verify=False)
        
    #     return response
    
    
    
#     # def put_changerequest(self,data):
        
#     #     url = f"{BASE_URL}/{self.idput}"
        
#     #     print("URL utilisée :", url)
        
#     #     response = requests.put(url, json=data , headers=self.headers , verify=False )
        
#     #     return response



    
#     # def delete_changerequest(self):
        
#     #     url =  f"{BASE_URL}/{self.idelete}"
#     #     print("URL utilisée :", url)
#     #     response = requests.delete(url, headers=self.headers , verify=False )
        
#     #     return response
    
    
    
#     # def get_listchangerequest(self):
        
#     #     url =  f"{BASE_URL}"
#     #     print("URL utilisée :", url)
#     #     response = requests.get(url, headers=self.headers , verify=False, params=self.paramslist)
        
#     #     return response
        
    

#     # def get_searchangerequest(self):
        
#     #     url =  f"{BASE_URL}"
#     #     print("URL utilisée :", url)
#     #     response = requests.get(url, headers=self.headers , verify=False, params=self.paramsearch)
        
#     #     return response 