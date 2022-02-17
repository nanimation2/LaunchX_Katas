# creacion de la lista

planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# se accede a la lista mediante su indice
print('The first planet is', planets[0])
print('The second planet is', planets[1])
print('The third planet is', planets[2])

# modificar elementos de la lista mediante indice
planets[3] = 'Red Planet'
print('Marz is also known as ', planets[3])

# saber la cantidad de elementos de una lista
number_of_planets = len(planets)
print(number_of_planets)

# agregar valores a la lista
planets.append('Pluto')
# para volver a contar los planetas ya modificados
number_of_planets = len(planets)
print('There are actully', number_of_planets,  'planets in the solar system')

# eliminar elementos de la lista
planets.pop()  # se elimina el ultimo elemento de la lista
number_of_planets = len(planets)
print('No, there are definitely', number_of_planets,
      'planets in the solar system.')

# los indices de la lista empiezan en 0
print("The first planet is", planets[0])

# indices negativos
# los indices negativos comiezan con -1 y este seria el ultimo elemento de la lista, el -2 el penultimo y asi
print('The last planet is', planets[-1])
print('The penultimate planet is', planets[-2])

# buscar elementos en una lista  (se utiliza index)
find_jupiter = planets.index('Jupiter')
print('Jupiter is the', find_jupiter + 1, 'planet from the sun')

# trabajar listas con numeros
# gravedad de la tierra y luna como referencia
gravity_on_earth = 1.0
gravity_on_the_moon = 0.166
# creacion de lista con numeros
gravity_on_planets = [0.378, 0.907, 1, 0.379, 2.36, 0.916, 0.889, 1.12]

# hacer operaciones con listas
bus_weight = 12650  # in kilograms, on Earth
print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
print('On Mercury, a double-decker bus weighs',
      bus_weight * gravity_on_planets[0], 'kg')

# funciones min() y max()
# estas funciones devuelven el numero mas pequeño y el mas grande respectivamente
bus_weight = 12650  # in kilograms, on Earth
print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
print('The lightest a bus would be in the solar system is',
      bus_weight * min(gravity_on_planets), 'kg')
print('The heaviest a bus would be in the solar system is',
      bus_weight * max(gravity_on_planets), 'kg')

# manipulacion de datos en una lista
# Slice list es para recuperar un fragmento de la lista como su nombre lo menciona, su funcionamiento es con el numero de indice inicial y final de elementos que queremos de la lista
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets_before_earth = planets[0:2]#los corchetes nos indican el slice y los numeros son los indices
print(planets_before_earth)

planets_after_earth = planets[3:8]
print(planets_after_earth) 

#uniendo listas
#estas son dos listas con lunas de jupiter galianas y alteanas
amalthea_group = ['Metis', 'Adrastea', 'Amalthea', 'Thebe']
galilean_moons = ['Io', 'Europa', 'Ganymede', 'Callisto']

regular_satellite_moons = amalthea_group + galilean_moons#aqui se estan uniendo las dos listas con el simbolo "+"
print('The regular satellite moons of Jupiter are', regular_satellite_moons)

##ordenando listas
##el metodo short ordena listas en orden alfabetico
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)