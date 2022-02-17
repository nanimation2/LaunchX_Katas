suma = 30+20
resta= 30-12
multiplicacion = 30*2
division = 30/2

print (suma, resta, multiplicacion, division)

##-----------------------------

segundos = 1042
conv_minutos = segundos // 60
res_segundos = segundos % 60
print(conv_minutos, res_segundos)

##------------------------------

result_1 = 1032 + 26 * 2
result_2 = 1032 + (26 * 2)
print(result_1, result_2)

##-----------------------
demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

##--------------------
a = 39 - 16
b = 16 - 39
print(a, b)

print(abs(39 - 16))
print(abs(16 - 39))

print(round(14.5))

##-------------------
from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)