from geopy.geocoders import Nominatim
import bs4
import requests


def buscarCiudad(ciudad):
    while True:
        try:
            loc = Nominatim(user_agent="informacionLocal")
            getLoc = loc.geocode(ciudad)
            
            if getLoc is None:
                ciudad = input('La localización buscada no se encuentra o no existe, indique algún dato más para una mejor búsqueda. ')
                continue  
            
            datos = getLoc.raw
            datosConcretos = datos['display_name']
            listaDatos = datosConcretos.split(', ')
    
            respuesta = input(f'¿{listaDatos[0]} de {listaDatos[1]}, país {listaDatos[-1]} es la localización que busca? sí o no: ').lower()
            
            if respuesta == 'si' or respuesta == 'sí':
                return listaDatos[0], listaDatos[-1]
            elif respuesta == 'no':
                ciudad = input('Escribe algún dato más de la localización para una mejor búsqueda: ')
            else:
                print('Sólo puede responder sí o no en este menú')
        except Exception as e:
            
            ciudad = input("Ha ocurrido un error introduce nuevamente el nombre de la localización: ")


