import os

class Configuracion:

    __slots__ = ()
    NOMBRE_AP = 'traductor-js'
    DESCRIPCION_AP = ' Traduce archivos de traducción «json».'
    VERSION = '2.2.0'
    CREDITOS = 'César Medina'
    
    DIR_EXE = os.getcwd() # directorio desde donde se ejecuta 
    
    # directorio de la aplicación
    DIR_APP = os.path.dirname(os.path.abspath(__file__))   
    DIR_ABS = DIR_APP+os.path.sep   
    
    # PID
    PID_FILE =  DIR_ABS+'pid.pid'
    
    MOTOR_DEFECTO = 'google'
    
    # MOTORES DE TRADUCCIÓN
    MOTORES = {
        'google': 'Google',
        'g': 'Google',  

        'deepl': 'DeepL',
        'd': 'DeepL',

        'libre': 'LibreT',
        'l': 'LibreT',
    }
    
  
   