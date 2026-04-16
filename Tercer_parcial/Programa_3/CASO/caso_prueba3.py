
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
        error_anterior= 0
        d = 0.5
        while True:
            integral = Integracion(self.x,self.dof)
            p_calculada = integral.calcularP(10) #Numero de segmentos
            error = self.p-p_calculada


            print(f'integral=♠{p_calculada}')
            print(f'x={self.x}')
            print(f'error={error}')
            print(f'd={d}')

            
            if abs(error) > tol:
                
                if error*error_anterior < 0:
                    d = d/2
                else:
                    d=d

                if p_calculada > self.p:
                    self.x = self.x-d
                   
                else:
                    self.x = self.x+d
                    
            else:
                
                break
            error_anterior = error