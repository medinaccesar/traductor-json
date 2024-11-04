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
        # TODO: Implementar traducción con DeepL 
        pass