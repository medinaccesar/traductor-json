from bs4 import BeautifulSoup
import requests
from constantes import Configuracion as conf
from service.traductor_service import Traductor

class TraductorGoogle(Traductor):

    def __init__(self):
        super().__init__()
        self._motor = conf.MOTORES.get('google')


    def traducir_texto(self, texto, source_lang, target_lang):   
        
        url = "https://translate.google.com/m?sl={}&tl={}&q={}".format(source_lang,target_lang, texto)
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        translation = soup.find('div', class_='result-container').text.strip()
    
        return translation