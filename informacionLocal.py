import funciones

while True:
    localizacion = input('Escribe el nombre del pueblo o ciudad que desea consultar: ')
    ciudad, pais = funciones.buscarCiudad(localizacion)
    amanecer, anochecer = funciones.consultarWeb(ciudad, pais)
    print(f'El amamecer esta previsto para las {amanecer} horas y el anochecer para las {anochecer} horas.')
    respuesta = input('Quieres consultar el amanecer de otra localización: ')
    if (respuesta.lower() in ['si', 'sí']):
        print('si')
    elif (respuesta.lower() == 'no'):
        print('Gracias por usar el programa.')
        break
    else:
        print('Sólo se puede contestar sí o no en éste menú')