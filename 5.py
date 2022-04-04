import math
from traceback import print_tb
V = 200
r_a = 0.1 
r_f = 0.1
I = float(input("Corrente: "))
N = 40
n = 900
f = 4000

E = V - ((r_a + r_f)*I)
print(E)
f_n = N*I
E_0 = f_n*V/f
velocidade = (E/E_0)*n

print("velocidade do motor em rpm = ", velocidade)

w = n*2*math.pi/60

k = E_0/w

print("conjugado = ", k*I)

v_n = float(input("nova tensao: "))
E_n = v_n - (r_a + r_f)*I

velocidade = (E_n/E_0)*n

print("nova velocidade do motor em rpm = ", velocidade)
