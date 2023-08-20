import funciones

try:
    ciudad = input("Escriba el nombre de la población o ciudad de la que desee consultar la hora de amanecer y atardecer:")
    print(funciones.buscarCiudad(ciudad))

except ValueError:
    print('la ciudad introducida no da resultados')