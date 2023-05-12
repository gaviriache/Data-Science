# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:27:33 2016

@author: L_Giocatore
"""

from filtro2_py import obtener_temps_por_mes, years
import matplotlib.pyplot as plt
import numpy as np


def grafico_temp_promedio(mes):
    
    vector = np.array(obtener_temps_por_mes(mes), dtype = float)
    vector_prom, vector_x = vector[:, 2], years(mes) 
        
    plt.figure(1,figsize = (9, 4.5), dpi = 90, facecolor = 'w', edgecolor = 'b')
    plt.plot(vector_x, vector_prom, 'o')
    plt.xlabel('years')
    plt.ylabel('Temperatura Promedio')
    plt.title('Gráfico de dispersión Tº')
    plt.hold(True)
    
    return plt.show()

#print(grafico_temp_promedio(7))
#------------------------------------------

def graph_errorbars(mes):
    
    vector = np.array(obtener_temps_por_mes(mes), dtype = float)
    vector_prom, vector_min, vector_max, vector_x = vector[:, 1], vector[:, 0], vector[:, 2], years(mes)
    
    plt.figure(2, figsize = (9, 4.5), dpi = 90, facecolor = 'w', edgecolor = 'b')
    plt.errorbar(vector_x, vector_prom, fmt= 'bo' , yerr=[vector_prom - vector_min, vector_max - vector_prom])
    plt.xlabel('years')
    plt.ylabel('Temperatura Promedio')
    plt.title('Gráfico Errorbar')    
    plt.savefig('Grafico.png')
    
    return plt.figure(2)
    

#print(graph_errorbars(1))       #Dos gráficas en una figura porque referencias la misma ventana figure()
#----------------------------------------------

def model_lineal(mes):
    
    graphic_2 = graph_errorbars(mes)
    print(graphic_2)
    plt.ioff()   
    vector = np.array(obtener_temps_por_mes(mes), dtype = float)
    vector_prom, vector_x = vector[:, 1], years(mes) 
    m, b = np.polyfit(vector_x, vector_prom, 1)
    
    plt.ion()
    plt.plot(vector_x, m * vector_x + b, 'r-')
    plt.savefig('Grafico_ajustado.png')    
    
    return plt.show()
   
#print(model_lineal(7))

#-------------------------


    
    