import json
from bs4 import BeautifulSoup
import requests
import os

def traducir_texto(texto, target_lang, source_lang):
    
    # TODO: gestionar distintos motores de traducción
    return google_translate(texto, target_lang, source_lang)

def google_translate(texto, target_lang, source_lang ):
    
    url = "https://translate.google.com/m?sl={}&tl={}&q={}".format(source_lang,target_lang, texto)
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    translation = soup.find('div', class_='result-container').text.strip()
    
    return translation

def procesar(fichero_fuente, fichero_destino, target_lang='es', source_lang='en' ):
    
    with open(fichero_fuente, 'r') as f:
        data = json.load(f)
    
    estructura_traducida = {}
    
    for key, value in data.items():
        if isinstance(value, str):  # Si es una cadena simple
            translated_value = traducir_texto(value,target_lang,source_lang)
            estructura_traducida[key] = translated_value
        elif isinstance(value, dict):  # Si es un diccionario
            translated_sub_dict = procesar_estructura_anidada(value,target_lang,source_lang)
            estructura_traducida[key] = translated_sub_dict
    
    with open(fichero_destino, 'w') as f:
        json.dump(estructura_traducida, f, indent=2)
    
    print(f"Se ha completado la traducción. Archivo de salida: {fichero_destino}")
    
def procesar_estructura_anidada(estructura, target_lang, source_lang):
    estructura_traducida = {}
    for key, value in estructura.items():
        if isinstance(value, str):
            estructura_traducida[key] = traducir_texto(value, target_lang,source_lang)
        elif isinstance(value, dict):
            estructura_traducida[key] = procesar_estructura_anidada(value,target_lang,source_lang)
        elif isinstance(value, list):
            estructura_traducida[key] = [traducir_texto(item,target_lang,source_lang) for item in value]
    return estructura_traducida   


if __name__ == "__main__":
    
    fichero_fuente = './en.json' 
    fichero_destino = './es.json'  
    
    procesar(fichero_fuente, fichero_destino)