
import os
from dotenv import dotenv_values
from constantes import Configuracion as Conf

class Fichero:
        
    def establecer_motor_traduccion_defecto(self, motor = Conf.MOTORES.get(Conf.MOTOR_DEFECTO), ruta_env =Conf.DIR_ABS + '.env'):
        if not self.existe_archivo_env():
           self.crear_archivo_env()
        env_vars = dotenv_values(ruta_env)
        env_vars['MOTOR'] = motor      
        self._escribir_fichero_diccionario(ruta_env,env_vars)

    def establecer_pausa(self, pausa = 0, ruta_env =Conf.DIR_ABS + '.env'):
        if not self.existe_archivo_env():
           self.crear_archivo_env()
        env_vars = dotenv_values(ruta_env)
        env_vars['PAUSA'] = str(pausa)
        self._escribir_fichero_diccionario(ruta_env,env_vars)

    def existe_archivo_env(self):
        ruta_env = Conf.DIR_ABS + '.env'
        return self.existe(ruta_env)  
    
    def existe(self,ruta):       
        if not os.path.isfile(ruta):
            return False       
        return True 
    
    def crear_archivo_env(self):        
        ruta_env = Conf.DIR_ABS + '.env'
        env_vars = {'IDIOMA': 'es', 'MOTOR': Conf.MOTORES.get(Conf.MOTOR_DEFECTO), 'PAUSA':0}
        self._escribir_fichero_diccionario(ruta_env,env_vars)

    def _escribir_fichero_diccionario(self,ruta,diccionario):
         with open(ruta, 'w') as archivo:
            for clave, valor in diccionario.items():
                archivo.write(f"{clave}={valor}\n")