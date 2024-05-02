from enum import Enum
class Silla:

    #-------------------------------------------
    # Enumeraciones
    #-------------------------------------------
    """Enumeradores para las clases de silla"""    
    
def TipoDeClase(Enum):
    #Representa la clase ejecutiva.
    claseEjecutiva = 8
    #Representa la clase económica.
    claseEconomica = 42
        
    """Enumeradores para las ubicaciones de las sillas"""

def TipoDeUbicaciones(Enum):

    #Representa la ubicación ventana
    Ventana = 18
    #Representa la ubicación centro
    Pasillo= 18
    #Representa la ubicación pasillo
    Central = 14
    
    #-------------------------------------------
    # Atributos
    #-------------------------------------------
    
    __Nombre = ""
    __Cedula = 0
    
    #-------------------------------------------
    # Metodos
    #-------------------------------------------
def __init__ (self, clase, ubicacion, pasajero, numero):
    self.__Clase = clase
    self.__Ubicacion = ubicacion
    self.__Pasajero = pasajero
    self.__Numero = numero

def __init__ ( self, pNumero, pClase, pUbicacion ):

    self.numero = pNumero
    self.clase = pClase
    self.ubicacion = pUbicacion
    self.pasajero = None

def asignarPasajero(self, pPasajero, pasajero ,sillasAsignadas,sillaDisponible):
    # Asigna la silla al pasajero "pPasajero"
    pasajero = pPasajero
    pPasajero == (self.nombre,self.cedula,self.TipoDeClase,self.TipoDeUbicacion)
    if TipoDeClase and TipoDeUbicaciones == sillaDisponible:
        sillaDisponible = pasajero
        return self.sillaDisponible  
    elif sillasAsignadas:
        return print('Error')
    
def desasignarSilla (self):
    # Quita al pasajero que se encuentra en la silla, dejándola desocupada. 
    self.pasajero = (TipoDeClase and TipoDeUbicaciones)
    return desasignarSilla

def sillaAsignada (self, nuevoPasajero,cedulaPasajero):
    # Informa si la silla está ocupada. 
    if self.sillaAsignada == nuevoPasajero:
        return nuevoPasajero
    elif not(cedulaPasajero):
        return print('Error')

def darNumero(self,sillasDesocupada,sillaOcupada):
    if self.numero == sillaOcupada:
        return sillaOcupada
    elif self.numero == sillasDesocupada:
        return sillasDesocupada
    
 #OTRA MANERA 
 
    CLASE = {
     'ventana':'Ventana',
     'centro':'Centro',
     'pasillo':'Pasillo'
    }
    
    UBICACION = {
        'ventana':'Ventana',
        'centro':'Centro',
        'pasillo':'Pasillo'
    }
    
    def __init__(self, pNumero, pClase, pUbicacion):
        self.numero = pNumero
        #Operador ternario forma 1 - operador pClase debe ser true or false
        self.clase = (self.CLASE.eje, self.CLASE.eco)[pClase]
        #Operador ternario forma 2
        self.clase = self.CLASE.eje if pClase =='Ejecutiva' else self.CLASE.eco
        #ESTRATEGIA TRADICIONAL
        if pUbicacion == 'ventana':
            self.__Ubicacion = self.UBICACION.ventana
        elif pUbicacion == 'centro':
            self.__ubicacion = self.UBICACION.centro
        elif pUbicacion == 'pasillo':
            self.__ubicacion = self.UBICACION.pasillo
        
        else: 
            self.__ubicacion = None
            
        self.__pasajero = None
        
    def asignarPasajero(self, pPasajero):
        self.__pasajero=pPasajero
    
    def designarSilla(self):
        self.__numero=None
        return True if self.__numero == None else False
    
    def getNumero (self):
        return self.__numero
    
    def getNumero(self):
        return self.__numero
    def
    
        