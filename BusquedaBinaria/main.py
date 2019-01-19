#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria

from archivos.leerArchivo import MiArchivo
from bbinaria.ArregloBinario import ArregloBinario

# Creamos un nuevo objeto para manejar el archivo
archivo = MiArchivo('datos/datos.txt')

# Variables
enteroABuscar = None
posicion = 0

# Obtenemos una lista de los datos del archivo
data = archivo.obtenerListaCompleta()
# Cerramos el archivo
archivo.cerrar_archivo()

# Creamos un objeto ArregloBinario y le pasamos los datos
# Este objeto ordena internamente los datos
arregloBusqueda = ArregloBinario(data)
# Mostramos los datos ordenados
print('\nLista ordenada:', arregloBusqueda)

# Ciclo de ingreso de datos
correcto = False
while not correcto:
    # Pedimos al usuario un numero entero
    try:
        enteroABuscar = int(input('Ingrese un numero a buscar: '))
    except ValueError as identifier:
        print('Ingresa un numero entero...')

    # Si la variable enteroABuscar es de tipo entero correcto se vuelve verdadero saliendo del ciclo
    if type(enteroABuscar) == int:
        correcto = True

# Pasamos el numero a buscar y nos retorna su posicion si lo encuentra
posicion = arregloBusqueda.busquedaBinaria(enteroABuscar)

# Presentamos el resultado
if posicion == -1:
    print('El entero %d no se encontro\n' % enteroABuscar)
else:
    print('El entero %d se encontro en la posicion %d.\n' %
          (enteroABuscar, posicion))
