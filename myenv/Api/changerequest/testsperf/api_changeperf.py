import requests
# from urllib.parse import urlparse
import json
from urllib.parse import urlparse, urlencode, parse_qs
import urllib.parse





class Apichange:
    
    
    base = "https://change-request.perfit.apps.dev.orange.local"
    
    pochange = "/api/changerequests"
    puchange = "/api/changerequests/7ad17c47-c2bd-45b0-bbba-1c1dec0379ab"
    getsearch = "Filters=state == 0"
    
    headers = {
        'content-type': 'application/json',
    }
    
    token = 'votre_token'  # Remplacez par votre token réel
    
    
    
    def __init__(self) -> None:
            self.token_a_to_invalidate = ''


    def sanitize_url(self,url):
        # Parse the URL to extract the query parameters
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        # Sanitize each parameter by removing unwanted characters
        for param, values in query_params.items():
            query_params[param] = [value.replace('&', '').replace(';', '').replace(' ','%20') for value in values]

        # Encode the sanitized parameters and reconstruct the URL
        sanitized_params = urlencode(query_params, doseq=True)
        sanitized_url = f'{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?{sanitized_params}'

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
    
    
    
    def get_changesearch(self, data):
        
    
        header = self.headers.copy()
        header['Authorization'] = self.token
        response = requests.request('GET', self.base+self.puchange, json=data, headers=header, verify=False, timeout=30)
        return response
    
         
    
    
    # def put_changeperf(self,data):
        
    #     header = self.headers.copy()
    #     header['Authorization'] = self.token
    #     response = requests.request('PUT', self.base, json=data, headers=header, verify=False, timeout=30)
    #     return response









# if __name__=='__main__':
#     p = Apichange()
#     # p.get_token()
#     # print(p.token_ama_to_invalidate)
#     # p.invalidate_token('ama')
    
#     for i in range(100):
#          p.post_changeperf()
    # print(p.token_ama_to_invalidate)
    
    # p.invalidate_token()