import pytest
import requests
import json
from config import AUTHORIZATION_TOKEN
from config import BASE_URL


def test_deletechange():
    
    headerDel = {
        'accept':'application/json',
        'Content-Type':'application/json',
        'Authorization': AUTHORIZATION_TOKEN
    }
    
    url = f"{BASE_URL}/9c8a0213-5f0c-408c-8be3-9071a8358df6"
    
   
    response = requests.get(url , headers = headerDel, verify=False )  # Remplacez par votre URL d'API
    
    
    assert response.status_code == 204
    