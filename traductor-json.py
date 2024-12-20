from service.fichero_service import Fichero
from service.traductor_service import Traductor
from service.motores.google_translate import TraductorGoogle
from service.motores.deepl_translate import TraductorDeepl
from service.motores.libre_translate import TraductorLibret
from utils.barra_progreso import BarraProgresoConsola
from utils.espannol_string_argparse import *
import argparse
from utils.locale_manager import _,p
from dotenv import load_dotenv
from constantes import Configuracion as Conf

class Principal:

    def __init__(self):              
        self._fichero = Fichero()
        self._traductor = self._crear_traductor()               
        self._procesar_argumentos()

    @staticmethod
    def _get_parser() -> argparse.ArgumentParser:

        parser = argparse.ArgumentParser(
            description=Conf.NOMBRE_AP + " " + str(Conf.VERSION))  # formatter_class=CustomHelpFormatter
        group = parser.add_mutually_exclusive_group()
        group.add_argument('-t', '--traducir', nargs=4,
                           metavar=(_('ARCHIVO'), _('ARCHIVO_TRADUCIDO'), _('IDIOMA_ORIGEN'),_('IDIOMA_DESTINO')), help=_('Traduce el archivo al idioma especificado'))
        group.add_argument(
            '-m', '--motor', action='store_true', help=_('Selecciona el motor de traducción por defecto'))

        group.add_argument('-p', '--pausa', type=str,
                           metavar=(_('PAUSA')), help=_('Ajusta la pausa entre peticiones'))
        group.add_argument(
            '-i', '--info', action='store_true', help=_('Muestra información con las opciones establecidas'))
        parser.add_argument('--version', action='version', version='%(prog)s ' +
                                                                   Conf.VERSION, help=_('Muestra la versión del programa'))

        return parser

    @staticmethod
    def _crear_traductor() -> Traductor:
       
        load_dotenv() 
        motor =  os.getenv('MOTOR', Conf.MOTORES.get(Conf.MOTOR_DEFECTO))
        pausa =  os.getenv('PAUSA', 0)

        traductores = {
            Conf.MOTORES.get('google')['nombre']: lambda: TraductorGoogle(),
            Conf.MOTORES.get('deepl')['nombre']: lambda: TraductorDeepl(),
            Conf.MOTORES.get('libre')['nombre']: lambda: TraductorLibret()
        }

        traductor = traductores.get(motor, lambda: TraductorGoogle())()
        traductor.set_pausa(pausa)
        return traductor
    
    def _establecer_motor_traduccion(self):
        
        motor = input('\n'+
            _('Elija el motor de traducción (Google/DeepL/libre) o (g/d/l)')+':')
        motor = Conf.MOTORES.get(motor.lower(), Conf.MOTORES.get(Conf.MOTOR_DEFECTO))
        self._fichero.establecer_motor_traduccion_defecto(motor)    
        return motor
    def _establecer_pausa(self, pausa):
         try:
            pausa = float(pausa)
         except ValueError:
            pausa = 0
         self._fichero.establecer_pausa(pausa)    
    def _procesar_argumentos(self):
            parser = self._get_parser()
            args = parser.parse_args()
       
            if args.motor is not None and args.motor is not False:   
                motor = self._establecer_motor_traduccion() 
                print(_('El motor de traducción por defecto es')+': ', motor, '\n')
               
            elif args.pausa is not None:
                self._establecer_pausa(args.pausa)
                print(_('La pausa se ha establecido correctamente.'),'\n') 
            elif args.info is not None and args.info is not False:               
                self._mostrar_info()
            
            elif args.traducir is not None:
                barra_progreso = BarraProgresoConsola(100)
                nombre_archivo, nombre_archivo_traducido, source_lang, target_lang = args.traducir                
                self._traductor.procesar(
                    nombre_archivo, nombre_archivo_traducido, source_lang,target_lang, barra_progreso.dibuja_bp)
              
                print('\n',_("Se ha completado la traducción. Archivo de salida: {nombre_archivo_traducido}").format(nombre_archivo_traducido=nombre_archivo_traducido))
            else:
                print(_('No se especificó ninguna opción'))   
        
    def _mostrar_info(self):
        if not self._fichero.existe_archivo_env():
                self._fichero.crear_archivo_env()               
        load_dotenv()      
        print(_('Opciones establecidas')+':')              
        print(_('Idioma de la aplicación')+':', os.getenv('IDIOMA'))
        print(_('Motor de traducción')+':',os.getenv('MOTOR'),'\n') 
        print(_('Pausa')+':',os.getenv('PAUSA'),'\n')     

if __name__ == "__main__":
    Principal()