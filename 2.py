import math
v = 250
I   = float(input("Corrente: "))
r_f = 180  #float(input("Resistencia de campo: "))
r_a = 0.2  #float(input("Resistencia de armadura: "))
RA  = 0.04 #float(input("Efeito desmagnetizante da reacao da armadura (RA): "))

i_f = v/r_f
i_a = I - i_f
E = v - (r_a*i_a)
print("Corrente para achar o valor de E no grafico = ", i_f - RA)
E_0 = float(input("E_0 = "))
n = float(input("n = "))
velocidade = E*n/E_0
print("velocidade do motor em rpm = ", velocidade)

perdas = float(input("perdas mecanicas: "))

P_e = E*i_a
P_out = P_e - perdas
print("rendimento = ", P_out*100/(v*I))

w = 2*math.pi*velocidade/60

print("Conjugado = ", P_out/w)


