from abc import ABCMeta, abstractmethod
import json
import time

class Traductor(metaclass=ABCMeta):

    def __init__(self):            
        self._motor = ''
        self._pausa = 0
        self._url = ''

    @abstractmethod
    def traducir_texto(self,texto, source_lang, target_lang):
        pass
   
    def procesar(self,fichero_fuente, fichero_destino, source_lang='en', target_lang='es',  callback = None ):
    
        with open(fichero_fuente, 'r') as f:
            data = json.load(f)
        
        estructura_traducida = {}
      
        long = len(data.items())
        incremento = 100 / long
                
        for clave, valor in data.items():
            if(callback):
                callback(incremento) 
            if isinstance(valor, str):  # Si es una cadena simple
                valor_traducido = self.traducir_texto(valor,source_lang,target_lang)
                estructura_traducida[clave] = valor_traducido
            elif isinstance(valor, dict):  # Si es un diccionario
                parte_traducida = self.procesar_estructura_anidada(valor,source_lang,target_lang)
                estructura_traducida[clave] = parte_traducida
    
        with open(fichero_destino, 'w') as f:
            json.dump(estructura_traducida, f, indent=2, ensure_ascii=False)       
      
    
    def procesar_estructura_anidada(self,estructura, source_lang, target_lang):
        estructura_traducida = {}
        for clave, valor in estructura.items():
            if isinstance(valor, str):
                estructura_traducida[clave] = self.traducir_texto(valor,source_lang, target_lang)
                self.pausar()
            elif isinstance(valor, dict):
                estructura_traducida[clave] = self.procesar_estructura_anidada(valor,source_lang,target_lang)
            elif isinstance(valor, list):
                estructura_traducida[clave] = []
                for item in valor:
                    valor_traducido = self.traducir_texto(item, source_lang, target_lang)
                    estructura_traducida[clave].append(valor_traducido)
                    self.pausar()
        return estructura_traducida  
    
    def get_motor(self):
        return self._motor

    def set_pausa(self, pausa):
        try:
            self._pausa = float(pausa)
        except ValueError:
            self._pausa = 0

    def pausar(self):
        if self._pausa > 0:
            time.sleep(self._pausa)

    def set_url(self, url):
        self._url = url
