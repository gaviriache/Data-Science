# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 17:41:58 2016

@author: mateo
"""

#Importacion de paquete contenedor de funciones - modulos y procedimientos

from filtro1_py import column_month, radiation_Dec, tempMin_year
from filtro2_py import obtener_temps_por_mes
import grafico_py as gr

#------------------------
print(column_month())
#------------------------
print(radiation_Dec())
#------------------------
print(tempMin_year())
#-----------------------1

mes = eval(input('Ingresa el numero del mes'))
print('---------------------')
print('T: max - prom - min')
print('---------------------')

while True:
    if mes <= 0 or mes > 12:
        mes = eval(input('Ingresa el numero del mes :'))
    else:
        break
#------------------------------------------   
print(obtener_temps_por_mes(mes))
#-------------------------------------------

print('-------------------------------')
print(gr.years(mes))
print('-------------------------------')
print(gr.grafico_temp_promedio(mes))
print('-------------------------------')
print(gr.graph_errorbars(mes))
print('----------------------')
print(gr.model_lineal(mes))
