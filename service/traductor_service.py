from abc import ABCMeta, abstractmethod
import json

class Traductor(metaclass=ABCMeta):

    def __init__(self):            
        self._motor = ''
   
    @abstractmethod
    def traducir_texto(texto, source_lang, target_lang):
        pass
   
    def procesar(self,fichero_fuente, fichero_destino, source_lang='en', target_lang='es',  callback = None ):
    
        with open(fichero_fuente, 'r') as f:
            data = json.load(f)
        
        estructura_traducida = {}
        
        for clave, valor in data.items():
            if isinstance(valor, str):  # Si es una cadena simple
                valor_traducido = self.traducir_texto(valor,source_lang,target_lang)
                estructura_traducida[clave] = valor_traducido
            elif isinstance(valor, dict):  # Si es un diccionario
                parte_traducida = self.procesar_estructura_anidada(valor,source_lang,target_lang)
                estructura_traducida[clave] = parte_traducida
    
        with open(fichero_destino, 'w') as f:
            json.dump(estructura_traducida, f, indent=2, ensure_ascii=False)
        
        #print(f"Se ha completado la traducción. Archivo de salida: {fichero_destino}")
    
    def procesar_estructura_anidada(self,estructura, source_lang, target_lang):
        estructura_traducida = {}
        for clave, valor in estructura.items():
            if isinstance(valor, str):
                estructura_traducida[clave] = self.traducir_texto(valor,source_lang, target_lang)
            elif isinstance(valor, dict):
                estructura_traducida[clave] = self.procesar_estructura_anidada(valor,source_lang,target_lang)
            elif isinstance(valor, list):
                estructura_traducida[clave] = [self.traducir_texto(item,source_lang,target_lang) for item in valor]
        return estructura_traducida  
    
    def getMotor(self):
        return self._motor