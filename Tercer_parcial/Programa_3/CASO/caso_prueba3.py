
from Segundo_parcial.Integracion_Num.integracion import Integracion

class Programa3(object):

    def __init__ (self, p,dof):
        self.p = p
        self.dof = dof
        self.x = 0

    def calcularX (self):
        #p_calculada = Integracion
        self.x = 1
        tol = 0.00001
        while True:
            integral = Integracion(self.x,self.dof)
            p_calculada = integral.calcularP(10) #Numero de segmentos
            error = self.p-p_calculada
            if abs(error) > tol:
                d = 0.5
                if p_calculada > self.p:
                    self.x = self.x-d
                    
                else:
                    self.x = self.x+d
                    
            else:
                
                break