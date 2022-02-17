#en este caso se generaran dos errores, uno indica que la funcion main no puede ejecutarse (basicamente por motivos del segundo error), y el segundo que no se encontro el archivo

# def main():
#     open("/path/to/mars.jpg")

# if __name__ == '__main__':
#     main()


##exepciones try
# try:#se intenta realizar lo que se indique en este bloque de codigo
#     open('config.text')
# except FileNotFoundError:#en caso de no poder ejecutarlo entra una exepcion y se ejecuta lo que este dentro del bloque
#     print("couldn't find the config.text file!")

# def main():
#     try:
#         configuation = open('config.text')
#     except:
#         print("couldn't find the config.text file!")

# if __name__ == '__main__': #The __name__ variable (two underscores before and after) is a special Python variable. It gets its value depending on how we execute the containing script.
#     main()
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")