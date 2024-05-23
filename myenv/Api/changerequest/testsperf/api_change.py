import requests
# from urllib.parse import urlparse






class Apichange:
    
    
    base = "https://change-request.perfit.apps.dev.orange.local/api/changerequests"
    
    
    headers = {
        'content-type': 'application/json',
    }
    
    token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJrSnRxNGNzNkRJRllNZFJ0TFMzeE5EcTNFN0M3UzBnWlVOeUZMQmYwZjVVIn0.eyJleHAiOjE3MTY0ODQzODgsImlhdCI6MTcxNjQ4MzQ4OCwiYXV0aF90aW1lIjoxNzE2NDgzNDQ4LCJqdGkiOiI1YTg5NWU5Yi02MDYwLTQxMDctYjZmOC0yYjAzMDBiOGQwMzAiLCJpc3MiOiJodHRwczovL2tleWNsb2FrLXByZXByb2QuYXBwcy5kZXYub3JhbmdlLmxvY2FsL3JlYWxtcy9kaWdpdGFsLWFwcCIsImF1ZCI6InBlcmZpdCIsInN1YiI6IjA0OWU0YjUxLWVhNWUtNDMxYy04ZTEwLTJlZmQ3OWE4YWIxMiIsInR5cCI6IklEIiwiYXpwIjoicGVyZml0Iiwibm9uY2UiOiIwYzg2NTM0Ny00NzY5LTQyZDQtODUzMy1lN2FmODBmNzc4YTkiLCJzZXNzaW9uX3N0YXRlIjoiOWFlYmM3YzctODlkMi00NzI4LTg5NjYtMDViMTgwN2Y2OTVmIiwiYXRfaGFzaCI6Ikc5ZC1Bd0l5OGdsb2NCZnk5WFRTNXciLCJzaWQiOiI5YWViYzdjNy04OWQyLTQ3MjgtODk2Ni0wNWIxODA3ZjY5NWYiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJLRU5HTkUgIEtFTkdORSIsInByZWZlcnJlZF91c2VybmFtZSI6InpiaHE4MzQ5IiwiZ2l2ZW5fbmFtZSI6IktFTkdORSAiLCJmYW1pbHlfbmFtZSI6IktFTkdORSIsImVtYWlsIjoidWxyaWNoLmtlbmduZUBvcmFuZ2UuY29tIn0.a4PnEAuJGxHh15Ol-P2Vy9Upsrwv5Xawr-3THpZUFZ5h8l-sn5pQGS3blPY26pvyJObArxIWLa8Wao0b56Hlu-onMOkQbts_7gFaN0rvlmzT3xO9bUloopOOBEKukICu4FtSt6NMdMJ1lmZ8pClb-GxSZRwx6NSHq6iYEnRAU8PFOeQn5Ru2ykMs6O0DngJlnwz1ct8JdNOwsYPqGKo1cJWF2gCPQ5H66HXBKwlfi4KcSiYQ45lR3mWECPDcTOBLUS8I62_Qbnwzn_aipDvPtS5sPq6dz4qGqTMl6ifLRt7tKD1I82ZYL-tlbfhN2lhIDUP6Ty5fFxRckwvGHBnP8w'



    # def __init__(self):
    #     parsed_url = urlparse(self.base)
        
        
        

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



    def post_change(self,data):
        
        header = self.headers.copy()
        header['Authorization'] = self.token
        response = requests.request('POST', self.base, json=data, headers=header, verify=False, timeout=30)
        return response
