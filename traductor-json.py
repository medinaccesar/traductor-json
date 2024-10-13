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
    print(translation)
    return translation

def procesar(fichero_fuente, fichero_destino, target_lang='es', source_lang='en' ):
    
    with open(fichero_fuente, 'r') as f:
        data = json.load(f)
    
    estructura_traducida = {}
    
    for clave, valor in data.items():
        if isinstance(valor, str):  # Si es una cadena simple
            valor_traducido = traducir_texto(valor,target_lang,source_lang)
            estructura_traducida[clave] = valor_traducido
        elif isinstance(valor, dict):  # Si es un diccionario
            parte_traducida = procesar_estructura_anidada(valor,target_lang,source_lang)
            estructura_traducida[clave] = parte_traducida
    
    with open(fichero_destino, 'w') as f:
        json.dump(estructura_traducida, f, indent=2, ensure_ascii=False)
    
    print(f"Se ha completado la traducción. Archivo de salida: {fichero_destino}")
    
def procesar_estructura_anidada(estructura, target_lang, source_lang):
    estructura_traducida = {}
    for clave, valor in estructura.items():
        if isinstance(valor, str):
            estructura_traducida[clave] = traducir_texto(valor, target_lang,source_lang)
        elif isinstance(valor, dict):
            estructura_traducida[clave] = procesar_estructura_anidada(valor,target_lang,source_lang)
        elif isinstance(valor, list):
            estructura_traducida[clave] = [traducir_texto(item,target_lang,source_lang) for item in valor]
    return estructura_traducida   

#TODO: permitir procesar argumentos
if __name__ == "__main__":
    
    fichero_fuente = './en.json' 
    fichero_destino = './es.json'  
    
    procesar(fichero_fuente, fichero_destino)