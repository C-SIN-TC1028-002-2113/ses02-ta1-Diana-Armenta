def main():
    #escribe tu código abajo de esta línea
    edad = int(input('Dame tu edad: '))
    actual = int(input('Dame el año actual: '))
    cumple = int((100 - edad) + actual)
    print('Cumplirás 100 años en el año:',cumple)



if __name__ == '__main__':
    main()
