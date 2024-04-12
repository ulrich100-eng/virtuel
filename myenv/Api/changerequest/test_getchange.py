import pytest
import requests
import json
from config import AUTHORIZATION_TOKEN
from config import BASE_URL


def test_getchange():
    
    headerGet = {
        'accept':'application/json',
        'Content-Type':'application/json',
        'Authorization': AUTHORIZATION_TOKEN
    }
    
    url = BASE_URL
    
   
    response = requests.get(url , headers = headerGet, verify=False )  # Remplacez par votre URL d'API
    
    
    assert response.status_code == 200
    