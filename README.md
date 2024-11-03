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

traductor-js 2.0.0

opciones:
  -h, --help            muestra este mensaje de ayuda y sale
  -t ARCHIVO ARCHIVO_TRADUCIDO IDIOMA_ORIGEN IDIOMA_DESTINO, --traducir ARCHIVO ARCHIVO_TRADUCIDO IDIOMA_ORIGEN IDIOMA_DESTINO
                        Traducir archivo
  -m, --motor           Selecciona el motor de traducción por defecto
  -i, --info            Muesta las opciones establecidas
  --version             Muestra la versión del programa
```
Por ejemplo:

* **Traducir un archivo :**
```
python traductor-json.py -t en.json es.json en es
Progreso |████████████████████████████████████████| 100% Completo
 Se ha completado la traducción. Archivo de salida: es.json
```
