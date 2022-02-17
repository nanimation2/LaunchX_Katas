#Aspectos básicos de las funciones de Python

#Funciones sin argumentos
from black import out


def rocket_parts():  #se def ine la funcion
    print('payload, propellant, structure')

output = rocket_parts()
print(output) ##se imprimira "none" porque la funcion no devuelve ningun valor

def rocket_parts():  #se def ine la funcion
    return 'payload, propellant, structure'
output = rocket_parts()
print(output) #se imprimiran los valores que regresa la funcion


##Argumentos opcionales y requeridos

any([True, False, False])

def distance_from_earth(destination):
    if destination == 'Moon':
        return '238,855'
    else:
        return 'Unable to compute to that destination'

print(distance_from_earth('moon'))