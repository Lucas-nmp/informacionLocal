from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup
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


def consultarWeb(poblacion, pais):
    if (pais == 'España'):
        pais = 'Spain'

    URL = (f'https://salidaypuestadelsol.com/sun/{poblacion}_({pais})')

    pedido_obtenido = requests.get(URL)
    html_obt = pedido_obtenido.text

    soup = BeautifulSoup(html_obt, 'html.parser')

    divs = soup.find_all('div', class_ = 'today-list__item-value font-weight-bold')

    return divs[0].text, divs[1].text