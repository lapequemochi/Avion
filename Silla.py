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
    