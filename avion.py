class Avion:
    SILLAS_EJECUTIVAS =8
    SILLAS_ECONOMICAS=42
     
    def __init__(self):
        self.sillasEjecutivas = []
        self.sillasEconomicas = []
        
    def __init__ (self):
        self.sillasEjecutivas =[]
        self.sillasEconomicas =[]
    
        self.sillasEjecutivas.append(1, Silla.CLASE.eje, Silla.UBICACION.ventana)
        self.sillasEjecutivas.append(2, Silla.CLASE.eje, Silla.UBICACION.pasillo)
    
    def definicionSillasEjecutivas(self):
        for i in range (self.SILLAS_EJECUTIVAS):