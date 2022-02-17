# user_input ='' ## declaracion de variable para que el usuario introdusca valor mas adelante
# while user_input.lower() != 'done':## mientras la entrada del usuario sea diferente a "done" hacer el ciclo
#     user_input = input('enter a new value, or done when done ')#se pide al usuario ingresar datos
    

# user_input = '' #volvemos a igualar user_imput a nada para que funcione el siguiente loop
# inputs = []

# while user_input.lower() != 'done':
#     if user_input:
#         inputs.append(user_input) #se almacenan todas las entradas diferentes a "done" que haga el usuario
#     user_input = input('Enter a new value, or done when done')
# print(inputs)


##---------------Ciclo for
##programa de cuenta regresiva
from time import sleep #libreria para hacer espera de 1 segundo

countdown=[4, 3, 2, 1, 0] #lista
for number in countdown: #pasa por cada indice de la lista countdown
    print(number)
    sleep(1)#hace una espera de 1 segundo

print("Blast off ")