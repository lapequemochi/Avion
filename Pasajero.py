class Pasajero:
    #-----------------------------------
    # Atributos
    #-----------------------------------
    Nombre = ""
    Apellido = ""
    Edad = 0
    Cedula = 0
    #-----------------------------------
    # Constructor
    #-----------------------------------
def __init__(self, pCedula, pNombre ):
    #Vamos a colocar los parámetros en privado 
    self.__Cedula=pCedula;
    self.__Nombre=pNombre

    #-----------------------------------
    # Métodos
    #-----------------------------------
def darCedula( self):
    #Aqui va el codigo
    return self.__Cedula

def darNombre( self  ):
    #Aqui va el codigo 
    return self.__Nombre 

    #Otra manera 
def getCedula(self):
    return self.__Cedula
def setCedula(self, pCedula):
    self.__Cedula = pCedula
def getNombre(self):
    return self.__Nombre
def setNombre(self, pNombre):
    self.__Nombre = pNombre
