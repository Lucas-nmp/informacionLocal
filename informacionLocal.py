import funciones

try:
    respuesta = ''
    intento = 0
    while respuesta != 'si':
        if (intento > 0):
            print('Escriba algún dato más de la población para una mejor busqueda')
        ciudad = input("Escriba el nombre de la población o ciudad de la que desee consultar la hora de amanecer y atardecer:")
        poblacion, pais = funciones.buscarCiudad(ciudad)
        respuesta = input('Es correcta la población buscada? (si o no)').lower
        intento += 1
        

except ValueError:
    print('la ciudad introducida no da resultados')