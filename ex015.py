print("CÁLCULO EQUAÇÃO SEGUNDO GRAU")
print("Qual o valor das A, B e C? ")
a = float(input())
b = float(input())
c = float(input())
import math 
delta = b**2 - 4*a*c
x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)
print("O valor de delta é:", delta)
print("O valor de x1 é:", x1)
print("O valor de x2 é:", x2)