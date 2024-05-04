from Silla import Silla
class Avion:
    SILLAS_EJECUTIVAS =8
    SILLAS_ECONOMICAS=42
     
    def __init__(self):
        self.sillasEjecutivas = []
        self.sillasEconomicas = []
        
    def __init__ (self):
        self.sillasEjecutivas =[]
        self.sillasEconomicas =[]
    
        self.sillasEjecutivas.append [1, Silla.CLASE.eje, Silla.UBICACION.ventana]
        self.sillasEjecutivas.append [2, Silla.CLASE.eje, Silla.UBICACION.pasillo]
    
    def definicionSillasEjecutivas(self):
        for i in range (self.SILLAS_EJECUTIVAS):
            if (i+1)%2 == 0:
                self.sillasEjecutivas.append (i+1) (1, Silla.CLASE.eje, Silla.UBICACION.ventana)
            else:
                self.sillasEjecutivas.append (i+1) (2, Silla.CLASE.eje, Silla.UBICACION.pasillo)
                
    def definicionSillasEConomicas(self):
        for i in range (self.SILLAS_ECONOMICAS):
            if (i+1)%2 == 43:
                self.sillasEjecutivas.append(i + 1)(1, Silla.CLASE.eco, Silla.UBICACION.ventana) and self.sillasEjecutivas.append(i + 1)(2, Silla.CLASE.eco, Silla.UBICACION.pasillo)  
            else:
                self.sillasEjecutivas.append(i + 1)(3, Silla.CLASE.eco, Silla.UBICACION.centro)
                
    def contarSillasEjecutivasOcupadas(self, sillaOcupada):
        for i in range (self.SILLAS_EJECUTIVAS):
            if self.sillasEjecutivas == sillaOcupada:
                sillaOcupada = +1
            return sillaOcupada
            
    def buscarPasajeroEjecutivo(self, pCedula, sillaPasajero):
       if sillaPasajero == pCedula:
           return sillaPasajero
       else:
           not (self.sillasEjecutivas(sillaPasajero(pCedula)))
           return None
       
    def buscarSillaEconomicaLibre(self, publicacion, sillaDisponible):
        if self.sillasEconomicas(self.TipoDeUbicaciones) == sillaDisponible:
            return publicacion
        else:
            not (sillaDisponible)
            return None
        
    def asignarSillaEconomica (self, pUbicacion, pPasajero, sillaDisponible):
        if self.sillasEconomicas == sillaDisponible:
            sillaDisponible == pPasajero and pUbicacion
            return True
        else:
            not sillaDisponible == pPasajero and pUbicacion
            return False
    
    def anularReservaEjecutica(self, pCedula, pPasajero):
        if self.sillasEjecutivas == pPasajero and pCedula:
            return True
        
    def contarVentanasEconomicas(self):
        for i in range(self.SILLAS_ECONOMICAS):
            if self.sillasEconomicas == self.TipoDeUbicacion:
                self.TipoDeUbicacion == self.ventana
                self.ventana = +1
            return self.ventana
    
    def hayDosHomonimosEcocnomica(self, pPasajeros, pCedulas, nombresIguales, patronDeDoble):
        if self.sillasEconomicas == pPasajeros:
            pPasajeros(pCedulas) == nombresIguales
            nombresIguales = patronDeDoble
            return patronDeDoble
    
        #Metodo 2
        
    def hayDosHomonimosEcocnomica(self, nombresIguales):
        nombres =[silla.pasajero.nombre for silla in self.sillasEconomicas]
        for nombre in nombresIguales:
            if nombres.count(nombre)>1:
                return True
            return False
    