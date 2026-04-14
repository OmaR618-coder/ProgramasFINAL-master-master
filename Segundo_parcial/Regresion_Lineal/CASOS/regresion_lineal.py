#CASOS-Caso_1.py
#TEST 1 X1,Y1
class Regresion_lineal():

    def __init__(self, dialog):
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

    def caso1(self):
        self.x = [130,650,99,150,128,302,95,945,368,961]
        self.y = [186,699,132,272,291,331,199,1890,788,1601]
        self.caso = 1
    
    def caso2(self):
        self.x = [130,650,99,150,128,302,95,945,368,961]
        self.y = [15,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2]
        self.caso = 2

    def caso3(self):
        self.x = [163,765,141,166,137,355,136,1206,433,1130]
        self.y = [186,699,132,272,291,331,199,1890,788,1601]
        self.caso = 3

    def caso4(self):
        self.x = [163,765,141,166,137,355,136,1206,433,1130]
        self.y = [15,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2]
        self.caso = 4
    def calcularRegresion(self):
        #SACAMOS XAVG
        """
        xavg = 0
        contadorN = 0
        """
        for i in self.x:
            self.xavg += i
            self.contadorN += 1
        self.xavg = self.xavg/self.contadorN
        """print("xavg = ",self.xavg )"""
        #B0 ERRONEO
        """self.dialog.showB0R.setText(str(self.xavg)) #nombre del label de qt"""

        #SACAMOS YAVG
        """
        yavg = 0
        contador2N = 0"""
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
        """
        x2 = 0"""
        for i in self.x:
            self.x2 += i**2
        print("x² =", self.x2)
       
        #sacamos xy
        """
        xy = 0"""
        for i in range(len(self.x)):
            self.xy += self.x[i]*self.y[i]
        print("x*y =", self.xy)

        #sacamos y²
        """
        y2 = 0"""
        for i in self.y:
            self.y2 += i**2
        print("y² =", self.y2)

        #CALCULAMOS B1
        self.B1 = (self.xy-(self.contadorN*self.xavg*self.yavg))/((self.x2)-(self.contadorN*self.xavg**2))
        """print("B1 =", "%.6f"%self.B1) #IMPRIMOS B1 CON 6 DECIMALES"""
        self.dialog.showB1A.setText(str(self.B1)) #nombre del label de qt

        #CALCULAMOS Rxy
        """
        self.rxy = (10*self.xy)-(self.xavg*self.yavg)
        self.rxy = self.rxy/(((10*self.x2)-(self.xavg**2))*((10*self.y2)-(self.yavg**2)))**(0.5)
        """
        numerador = (self.contador2N * self.xy) - (self.sum_x * self.sum_y)
        denominador = ((self.contador2N * self.x2) - (self.sum_x ** 2)) * ((self.contador2N * self.y2) - (self.sum_y ** 2))
        denominador = denominador ** 0.5
        self.rxy = numerador / denominador

        match self.caso:
            case 1:
                self.dialog.showB0R.setText(str(-22.55)) #VALOR REAL TEST 1 B0
                self.dialog.showB1R.setText(str(1.7279)) #VALOR REAL TEST 1 B1
                self.dialog.showrxyR.setText(str(0.9545)) #VALOR REAL TEST 1 RXY
                self.dialog.showr2R.setText(str(0.9111))#VALOR REAL TEST 1 R2
                self.dialog.showykR.setText(str(644.429)) #VALOR REAL TEST 1 YK

            case 2:
                self.dialog.showB0R.setText(str(-4.039)) #VALOR REAL TEST 2 B0
                self.dialog.showB1R.setText(str(0.1681)) #VALOR REAL TEST 2 B1
                self.dialog.showrxyR.setText(str(0.9333)) #VALOR REAL TEST 2 RXY
                self.dialog.showr2R.setText(str(0.8711))#VALOR REAL TEST 2 R2
                self.dialog.showykR.setText(str(60.858)) #VALOR REAL TEST 2 YK
                
            case 3:
                self.dialog.showB0R.setText(str(-23.92)) #VALOR REAL TEST 3 B0
                self.dialog.showB1R.setText(str(1.43097)) #VALOR REAL TEST 3 B1
                self.dialog.showrxyR.setText(str(0.9631)) #VALOR REAL TEST 3 RXY
                self.dialog.showr2R.setText(str(0.9276))#VALOR REAL TEST 3 R2
                self.dialog.showykR.setText(str(528.4294)) #VALOR REAL TEST 3 YK

            case 4:
                self.dialog.showB0R.setText(str(-4.604)) #VALOR REAL TEST 4 B0
                self.dialog.showB1R.setText(str(0.140164)) #VALOR REAL TEST 4 B1
                self.dialog.showrxyR.setText(str(0.9480)) #VALOR REAL TEST 4 RXY
                self.dialog.showr2R.setText(str(0.8988))#VALOR REAL TEST 4 R2
                self.dialog.showykR.setText(str(49.4994)) #VALOR REAL TEST 4 YK

        #Ya calculado RXY LO MOSTRAMOS      
        self.dialog.showrxyA.setText(str(self.rxy)) #nombre del label de qt
        
        #CALCULAMOS R²
        self.r2 = self.rxy*self.rxy
        self.dialog.showr2A.setText(str(self.r2)) #nombre del label de qt

        #CALCULAMOS B0
        self.B0 = self.yavg-self.xavg*self.B1
        self.dialog.showB0A.setText(str(self.B0)) #nombre del label de qt

        #CALCULAMOS YK SABIENDO QUE XK ES 386
        self.yk  =self.B0+self.B1*386
        self.dialog.showykA.setText(str(self.yk)) #nombre del label de qt
       
