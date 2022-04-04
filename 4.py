import math
from tkinter import W
n = 1800
i_f = 2
V = 250
r_f = 125
r_a = 1
I = float(input("Corrente: "))
R = float(input("Resistencia do reostato: "))

i_f_n = V/r_f

E_0 = V*i_f_n/i_f

i_a = I - i_f_n

E = V - r_a*i_a

velocidade = E*n/E_0
print("velocidade do motor em condicoes nominais em rpm = ", velocidade)
w = velocidade*2*math.pi/60
print("velocidade do motor em condicoes nominais em rad/s = ", w)

k = E_0/(n*2*math.pi/60)
conjugado = k*i_a
print("conjugado = ", conjugado)

i_f_n = V/(r_f+R)
i_a_n = i_f*i_a/i_f_n
k_n = conjugado/i_a_n
E_n = V - i_a_n*r_a
w_n = E_n/k_n
velocidade_n = 60*w_n/(2*math.pi)

print("velocidade do motor com reostato em rpm = ", velocidade_n)