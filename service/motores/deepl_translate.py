from bs4 import BeautifulSoup
import requests
from constantes import Configuracion as conf
from service.traductor_service import Traductor

class TraductorDeepl(Traductor):

    def __init__(self):
        super().__init__()
        self._motor = conf.MOTORES.get('deepl')
        self._API_KEY = 'TU_API_KEY' # leer de .env


    def traducir_texto(self, texto, source_lang, target_lang):   
          
        url = "https://api-free.deepl.com/v2/translate"
        params = {
            "auth_key": self._API_KEY,
            "text": texto,
            "target_lang": target_lang,
            "source_lang": source_lang
        }
       
        response = requests.post(url, data=params)
        
        if response.status_code == 200:
            translation = response.json()
            return translation['translations'][0]['text']
        else:           
            return ''