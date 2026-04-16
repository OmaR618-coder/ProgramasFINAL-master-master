import math 
import numpy as np

class Programa4():

    def __init__(self, dialog):

        #REGRESION VARIABLES
        self.x = []
        self.y = []
        self.xavg=0
        self.sum_x=0
        self.contadorN=0
        self.yavg=0
        self.sum_y=0
        self.contador2N=0
        self.x2=0
        self.xy=0
        self.y2=0
        #SHOW
        self.B1=0
        self.rxy=0
        self.r2=0
        self.B0=0
        self.yk=0
        self.dialog = dialog
        self.caso=0

        self.n = 10
        #INTEGRACION VARIABLES
        
        self.dof = self.n-2
        self.num_seg = 10

        #p4
        self.calcularX  = calcularX()
    def caso1(self):
        self.x = [130,650,99,150,128,302,95,945,368,961]
        self.y = [186,699,132,272,291,331,199,1890,788,1601]
        self.caso = 1
    
    def caso2(self):
        self.x = [130,650,99,150,128,302,95,945,368,961]
        self.y = [15,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2]
        self.caso = 2

    def calcularRegresion(self):

        for i in self.x:
            self.xavg += i
            self.contadorN += 1
        self.xavg = self.xavg/self.contadorN

        #SACAMOS YAVG
        for i in self.y:
            self.yavg += i
            self.contador2N += 1
        self.yavg = self.yavg/self.contador2N
        print("yavg = ",self.yavg )

        #SACAMOS SUM_X
        self.sum_x= self.xavg * 10

        #SACAMOS SUM_Y
        self.sum_y = self.yavg *10 

        #sacamos x²
        for i in self.x:
            self.x2 += i**2
        print("x² =", self.x2)
       
        #sacamos xy
        for i in range(len(self.x)):
            self.xy += self.x[i]*self.y[i]
        print("x*y =", self.xy)

        #sacamos y²
        for i in self.y:
            self.y2 += i**2
        print("y² =", self.y2)

        #CALCULAMOS B1
        self.B1 = (self.xy-(self.contadorN*self.xavg*self.yavg))/((self.x2)-(self.contadorN*self.xavg**2))

        #CALCULAMOS Rxy
        numerador = (self.contador2N * self.xy) - (self.sum_x * self.sum_y)
        denominador = ((self.contador2N * self.x2) - (self.sum_x ** 2)) * ((self.contador2N * self.y2) - (self.sum_y ** 2))
        denominador = denominador ** 0.5
        self.rxy = numerador / denominador
        
        #CALCULAMOS R²
        self.r2 = self.rxy*self.rxy

        #CALCULAMOS B0
        self.B0 = self.yavg-self.xavg*self.B1

        #CALCULAMOS YK SABIENDO QUE XK ES 386
        self.yk  =self.B0+self.B1*386
    
    def calcular_x_new(self):
        self.x_new = (abs(self.rxy)*(self.n-2)**0.5)/(1-self.rxy**2)**0.5
        self.x_new_abs = abs(self.x_new)

    def calcularF(self, x):
        numerador = math.gamma((self.dof + 1) / 2)
        denominador = ((self.dof * math.pi)**0.5) * math.gamma(self.dof / 2)
        numdem = numerador / denominador
        exp = -((self.dof + 1) / 2)
        return numdem * (1 + ((x**2) / self.dof))**exp

    def calcularP(self, num_seg):
        if num_seg % 2 != 0:
            num_seg += 1

        acum = 0
        w = self.x / num_seg

        for i in range(1, num_seg):
            if i % 2 == 0:
                acum += 2 * self.calcularF(i * w)
            else:
                acum += 4 * self.calcularF(i * w)

        return (w / 3) * (self.calcularF(0) + acum + self.calcularF(self.x))

    def iterar(self):
        tol = 1e-7
        n = self.num_seg
        p1 = self.calcularP(n)

        while True:
            n *= 2
            p2 = self.calcularP(n)
            error = abs(p2 - p1)

            if error < tol:
                return p2
            else:
                p1 = p2

    def tail_area(self):
        self.x = self.x_new_abs
        self.dof = self.n - 2
        p = self.iterar()

        tail_area = 1-2*p
        print(tail_area)
        
    def rango(self):
        s = np.sum((self.y-self.B0-self.B1*self.x)**2)
        sigma = (1/8*s)**0.5 #1/8 = 1/n-2
        r = 1+0.1+(self.x-self.xavg)**2/np.sum((self.x-self.xavg)**2)#0.2 = 1/n osea 1/10
        rango = self-calcularX(0.35,8) *sigma*(r**0.5) #8 = n-2 y corresponde a dof

    def upi_lpi(self):
        self.yk - 0.7*rango
