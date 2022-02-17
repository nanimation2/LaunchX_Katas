#Usar una estructura de diccionario dentro de la aplicación para almacenar datos en un formato que facilite la búsqueda de valores.
##En este módulo, crearás un programa que puede realizar estos tipos de operaciones. Utilizaremos diccionarios de Python para modelar los datos. Al final del módulo, podrás trabajar con diccionarios de Python para almacenar datos complejos.
planet = {  ##creacion del diccionario
    'name': 'Earth', ##contiene el dato nombre y el dato lunas
    'moons': 1
} 

##leer valores del diccionario
print(planet.get('name'))

#Modificación de valores de un diccionario
planet.update({'name': 'Makemake'})
planet['name'] = 'Makemake'

planet.update({
    'name': 'Jupiter',
    'moons': 79
})

##adicion de claves
planet['orbital period'] = 4333
# el diccionario planet ahora contiene: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }

#eliminacion de claves
planet.pop('orbital period')

# el diccionario planet ahora contiene: {
#   name: 'jupiter'
#   moons: 79
# }

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

