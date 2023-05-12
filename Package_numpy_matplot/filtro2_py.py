# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 15:25:08 2016

@author: L_Giocatore
"""

from numpy import array, loadtxt, float

def obtener_temps_por_mes(mes):     #función retorna un vector creado a partir de un condicional
    #Variable data carga archivo - temps crea sub_vector de la lista data a partir del rango de columnas de temperatura
    #Variable l_temp_month inicialmente es una lista que almacena cada registro de temperaturas en una posición, -
    #si el valor del data en la columna mes, coincide con el valor del argumento de la función
    data = loadtxt('mult_data.csv', delimiter = ',', skiprows = 1)
    temps, l_temp_month, k = array(data[:, 2:5], dtype = float), [], 0
       
    while k < len(data[:, 1]):
        if data[k, 1] == mes:                     #valor del mes en registro especifico del data coincide con argumento
            l_temp_month.append(temps[k, :])      #capturar el registro especifico de temperaturas para el mes indicado   
        k += 1
    
    l_temp_month = array(l_temp_month, dtype = float).reshape((len(l_temp_month), 3))  #convertir lista a array.reshape
    
    if __name__ == "__main__":
        print('---------------------')
        print('T: max - prom - min')
        print('---------------------')
    
    return l_temp_month     
     

#print(obtener_temps_por_mes(7))

def years(mes):
    
    data = loadtxt('mult_data.csv', delimiter = ',', skiprows = 1)
    vector_year, lista, k = array(data[:, 0], dtype = int), [], 0
    
    while k < len(vector_year):
        if data[k, 1] == mes:
            lista.append(vector_year[k])
        k += 1
        
    lista = array(lista, dtype = int)
    
    return lista
    