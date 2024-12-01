from bs4 import BeautifulSoup
import requests
from constantes import Configuracion as conf
from service.traductor_service import Traductor


class TraductorLibret(Traductor):

    def __init__(self):
        super().__init__()
        self._motor = conf.MOTORES.get('libre')['nombre']
        # TODO: leer de .env
        #  Motor sin API_KEY pero que acepta 5 pet./min, pausa = 12 segundos
        # "https://trans.zillyhuhn.com/translate"
        self._url = 'https://libretranslate.com/translate'  # Necesita API_KEY
        self._ALTERNATIVES = 0
        self._API_KEY = ''


    def traducir_texto(self, texto, source_lang, target_lang):   


        url = self._url  
        params = {
            "api_key": self._API_KEY,
            "q": texto,
            "target": target_lang,
            "source": source_lang,
            "alternatives":  self._ALTERNATIVES,
        }


        try:
            response = requests.post(url, json=params)            
            translation = response.json()    
            if response.status_code == 400 or response.status_code == 403 or response.status_code == 429:
              print('Error:',translation['error'])           
            response.raise_for_status()  
            return translation['translatedText']
        except requests.exceptions.RequestException as e:
            print(f"Fallo al realizar la solicitud: {e}")
            exit() 
            