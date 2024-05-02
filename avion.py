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
    
        self.sillasEjecutivas.append (1, Silla.CLASE.eje, Silla.UBICACION.ventana)
        self.sillasEjecutivas.append (2, Silla.CLASE.eje, Silla.UBICACION.pasillo)
    
    def definicionSillasEjecutivas(self):
        for i in range (self.SILLAS_EJECUTIVAS):
            if (i+1)%2 == 0:
                self.sillasEjecutivas.append((i+1) 1, Silla.CLASE.eje, Silla.UBICACION.ventana)
            else:
                self.sillasEjecutivas.append((i+1) 2, Silla.CLASE.eje, Silla.UBICACION.pasillo)
                
    def definicionSillasEConomicas(self):
        for i in range (self.SILLAS_ECONOMICAS):
            if (i+1)%2 == 0:
                self.sillasEjecutivas.append((i + 1, Silla.CLASE.eco, Silla.UBICACION.ventana))
                self.sillasEjecutivas.append((i + 1, Silla.CLASE.eco, Silla.UBICACION.pasillo))
            else:
                self.sillasEjecutivas.append((i + 1, Silla.CLASE.eco, Silla.UBICACION.centro))
            
    