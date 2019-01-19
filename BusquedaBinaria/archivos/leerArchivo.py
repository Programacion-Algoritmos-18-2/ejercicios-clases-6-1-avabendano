#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria

import codecs
import sys


class MiArchivo:

    # Constructor de clase, recibe una ruta de archivo
    def __init__(self, path):
        self.path = path
        self.archivo = codecs.open(self.path, "r")

    # Metodo que devuelve una lista de todos los elementos numericos que encuentra en el archivo
    def obtenerListaCompleta(self):
        listaCompleta = []
        # Guardamos una lista de todas las lineas del archivo
        informacion = self.archivo.readlines()

        # Recorremos cada linea y separamos sus valores
        for linea in informacion:
            datos = linea.split(',')
            # Recorremos cada valor y lo añadimos a la lista
            for dato in datos:
                listaCompleta.append(int(dato))

        # Retornamos la lista con todos los valores
        return listaCompleta

    # Metodo que cierra el archivo
    def cerrar_archivo(self):
        self.archivo.close()
