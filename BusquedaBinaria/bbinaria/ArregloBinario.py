#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria


class ArregloBinario(object):

    # Atributo global
    datos = []

    # Constructor de clase
    def __init__(self, datos):
        self.agregarDatos(datos)

    # Metodo que almacena los datos y los ordena
    def agregarDatos(self, datos):
        self.datos = datos
        # Ordenacion de los datos
        self.datos.sort()

    # Metodo de busqueda binaria
    def busquedaBinaria(self, elemento):
        inferior = 0
        superior = len(self.datos) - 1
        medio = int((inferior + superior + 1) / 2)
        ubicacion = -1

        # Ciclo principal
        while (inferior <= superior) and (ubicacion == -1):
            if elemento == self.datos[medio]:
                ubicacion = medio
            elif elemento < self.datos[medio]:
                superior = medio - 1
            else:
                inferior = medio + 1

            medio = int((inferior + superior + 1) / 2)

        # Retornamos la posicion del elmeento
        return ubicacion

    # Metodo __str__ sobreescrito
    def __str__(self):
        temporal = ''
        for elemento in self.datos:
            temporal = '%s %s' % (temporal, elemento)
        temporal = '%s %s' % (temporal, '\n')
        return temporal
