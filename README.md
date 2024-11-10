# traductor-json
Traduce ficheros de idiomas de formato «json».

# Requisitos
 Python 3.
 
# Instalación de dependencias

```
 pip install -r requirements.txt
 ```
# Uso

```
Uso: traductor-json.py [-h] [-t ARCHIVO ARCHIVO_TRADUCIDO IDIOMA_ORIGEN IDIOMA_DESTINO | -m | -i] [--version]

traductor-js 2.1.0

opciones:
  -h, --help            muestra este mensaje de ayuda y sale
  -t ARCHIVO ARCHIVO_TRADUCIDO IDIOMA_ORIGEN IDIOMA_DESTINO, --traducir ARCHIVO ARCHIVO_TRADUCIDO IDIOMA_ORIGEN IDIOMA_DESTINO
                        Traduce el archivo al idioma especificado
  -m, --motor           Selecciona el motor de traducción por defecto
  -i, --info            Muestra información con las opciones establecidas
  --version             Muestra la versión del programa
```
Por ejemplo:

* **Traducir un archivo :**
```
python traductor-json.py -t en.json es.json en es
Progreso |████████████████████████████████████████| 100% Completo
 Se ha completado la traducción. Archivo de salida: es.json
```

# Traducciones / Translations
Se puede usar como base ./locale/template.po y con «poedit» u otro editor rellenar las traducciones.  El archivo se coloca dentro de la carpeta correspondiente, por ejemplo para portugués en ./locale/pt/LL_MESSAGES/:

```
traductor-json/
├─ README.md
├─ traductor-json.py
├─ ...
├─ locale/
│  ├─ pt/    
│  │   └─ LL_MESSAGES/
│  │        pt.po
│  ├─ ...
|
├─ ...  
```
Posteriormente se compila el archivo de traducción ejecutando:
```
python ./utils/compile_lang.py 
```
El idioma de la aplicación se fija en el archivo .env:
```
IDIOMA = 'es'
```

[EN] You can use as a base ./locale/template.po and with "poedit" or another editor fill in the translations.  The file is placed inside the corresponding folder, for example for Portuguese in ./locale/pt/LL_MESSAGES/:
```
traductor-json/
├─ README.md
├─ traductor-json.py
├─ ...
├─ locale/
│  ├─ pt/    
│  │   └─ LL_MESSAGES/
│  │        └─pt.po
│  ├─ ...
|
├─ ...  
```
Subsequently, the translation file is compiled by executing:
```
python ./utils/compile_lang.py 
```
The application language is set in the .env file:
```
IDIOMA = 'pt'
```