from geopy.geocoders import Nominatim
import bs4
import requests



def buscarCiudad(ciudad):
    #
    loc = Nominatim(user_agent="informacionLocal")
 
    # 
    getLoc = loc.geocode(ciudad)
    
    datos = getLoc.raw
    datosConcretos = datos['display_name']
    listaDatos = datosConcretos.split(', ')
    print(listaDatos)
    #print(f'La localización buscada es {listaDatos[0]}, de {listaDatos[1]}, con el código postal {listaDatos[-2]}, {listaDatos[-1]}?')
    # return (f'La localización buscada es {listaDatos[0]}, de {listaDatos[1]}, con el código postal {listaDatos[-2]}, {listaDatos[-1]}?')
    return listaDatos[0], listaDatos[-1]

