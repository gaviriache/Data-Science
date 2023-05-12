# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 23:54:40 2016

@author: L_Giocatore

"""
import numpy as np

def column_month():     #Función de retorno del subvector mes(segunda columna de la lista del archivo)
    #Variable 'data' contiene instrucción que carga el archivo a memoria
    #Variable month extrae todo el rango de meses contenidos en la segunda columna del arreglo data
    data = np.loadtxt('mult_data.csv', delimiter = ',', skiprows = 1)
    month = np.array(data[:,1], dtype = int)  #crea sub_vector tipo entero con las componentes de la columna 2 de la lista data
        
    return month
    
#----------------------------------------------
    
def radiation_Dec():        #Función de impresión de las radiaciones que corresponden a Diciembre de cada año
    #Variable data carga el archivo csv -- Variable month,year contienen subarrays del data, K será un contador
    data = np.loadtxt('mult_data.csv', delimiter = ',', skiprows = 1)
    month, year, k = np.array(data[:,1], dtype = np.int), np.array(data[:,0], dtype = int), 0
    radiation = np.array(data[:,6], dtype = float) #sub_vector de radiación
    print('------------------------------------------------------------')
    while k < len(month):   #Bucle  de comparación de cada valor del array month con el mes 12
        #Impresión de las radiaciones relacionadas a al mes de Diciembre de cada año.
        if month[k] == 12:
            print('Radiación correspondiente a Diciembre de ', year[k], '-:- ', radiation[k])
        k += 1    
    print('-------------------------------------------------------------')

#-------------------------------------------------------

def tempMin_year():     #función que crea un subarray a partir de un rango de filas y la columna de temperaturas min.
    #Variable temp_min crea el subarreglo tipo float y lo reforma a una matriz ordenadas de filas por meses del año
    #El rango 514:742 contiene los años comprendidos entre 1981 y 1999. - Indice 4 referencia la columna de temp_min
    data = np.loadtxt('mult_data.csv', delimiter = ',', skiprows = 1)
    temp_min = np.array(data[514:742, 4], dtype = float).reshape((19, 12))
    print('Las temperaturas minimas por mes, comprendidas entre el rango \n de años 1981-1999 corresponden a continuación: ')
    print('------------------------------------------------------')
    
    return temp_min



