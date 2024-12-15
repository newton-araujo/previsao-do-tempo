import requests


def previsao_atual(city):
    
    KEY = '2ff2570de3184e85a3521119241412'
    BASE_URL = 'http://api.weatherapi.com/v1'
    
    endpoint = f"{BASE_URL}/current.json"
    
    params = {
        "key":KEY,
        "q":city,
        "lang":"pt"
    }
    
    try:
        
        response = requests.get(endpoint,params=params)
        response.raise_for_status()
        
        data = response.json()
        
        return data

    except requests.exceptions.RequestException as e:
        return f"Erro ao acessar a API: {e}"
    
    
