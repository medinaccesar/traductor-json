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
    MOTOR_GOOGLE = {
         'nombre': 'Google', 
    }
    MOTOR_DEEPL = {
        'nombre': 'DeepL',        
        'API_KEY': '',   
    }
    MOTOR_LIBRE = {
        'nombre': 'LibreT',
        'alternatives': 5,
        'API_KEY': '',   
        'URL': '' 
    }

    MOTORES = {
        'google': MOTOR_GOOGLE,
        'g': MOTOR_GOOGLE,  

        'deepl': MOTOR_DEEPL,
        'd': MOTOR_DEEPL,

        'libre': MOTOR_LIBRE,
        'l': 'MOTOR_LIBRE',
    }
  
   