#place this code on a folder called quadratic
#name the file Class_quadratic.py
import math
class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def discriminant(self):
        return ((self.b)**2) - (4 * self.a * self.c)

    def x1(self):
        if self.discriminant() < 0:
            istr = "imaginary"
            return istr
        else:
            return (-self.b + math.sqrt(self.discriminant())) / (2 * self.a)

    def x2(self):
        if self.discriminant() < 0:
            istr = "imaginary"
            return istr
        else:
            return (-self.b - math.sqrt(self.descriminant())) / (2 * self.a)

if __name__ == "__main__":
    p1 = QuadraticEquation(1,0,9)
    x1 = p1.x1()
    x2 = p1.x2()
    print ("discriminant = ",p1.discriminant())
    print ("x1 = ",x1," x2 = ",x2)

"""
The line if __name__ == "__main__":
tells the program that the code inside this
"""
