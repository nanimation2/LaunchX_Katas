# generará un error tracebak el error es FileNotFoundError, como su nombre lo dice no se encontró el archivo
#open("/path/to/mars.jpg")

#en este caso se generaran dos errores, uno indica que la funcion main no puede ejecutarse (basicamente por motivos del segundo error), y el segundo que no se encontro el archivo

def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main()

    