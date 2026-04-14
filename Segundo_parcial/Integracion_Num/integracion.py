import math

class Integracion(object):
    def __init__(self, x, dof):
        self.x = abs(x)
        self.dof = dof
        self.num_seg = 10

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

    
