import math
V = 220 
I = 150 
r_a = 0.02 
r_f = 0.02
N = 10
RA = 75
n = 900
E = V - (r_a + r_f)*I
print("forca para achar o E na curva: ", N*I - RA)
E_0 = 0.065*(N*I - RA) + 35
velocidade = E*n/E_0
print("velocidade do motor em condicoes nominais em rpm = ", velocidade)
print("velocidade do motor em condicoes nominais em rad/s = ", velocidade*2*math.pi/60)

perdas = float(input("perdas = "))
P_e = E * I
P_out = P_e - perdas
print("Rendimento = ", P_out/(V*I))

I_n = float(input("Corrente: "))
E_n = V - (r_a + r_f)*I_n
RA_n = I_n*RA/I
print("forca para achar o E na curva: ", N*I_n - RA_n)
E_0_n = 0.065*(N*I_n - RA_n) + 35
velocidade_n = E_n*n/E_0_n
print("velocidade do motor em condicoes nominais em rpm = ", velocidade_n)
w = 2*math.pi*velocidade_n/60
print("velocidade do motor em condicoes nominais em rad/s = ", w)

perdas_w = float(input("perdas rotacionais = "))
P_e = (E_n*I_n) - perdas_w
print("Conjugado = ", P_e/w)
