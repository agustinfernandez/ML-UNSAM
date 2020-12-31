#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 10:40:15 2020

@author: agustin18
"""

# Preparamos todo para correr
import numpy as np
from math import *
from matplotlib import pyplot as plt
import pandas as pd

#%%

#Ejercicios_python_ML

#a. Cree un array de numpy de 10x10 cuyos elementos estén distribuidos de manera uniforme entre 1 y 3.

matriz = np.random.randint(1,4,(10,10))
print(matriz)

#%%

#b. A partir de este array, cree un array unidimensional que contenga todos los elementos de la diagonal.

b = np.diagonal(matriz)
#print(b)



#%%

#c. Determine si la matriz es inversible y de serlo obtenga sus autovalores y autovectores utilizando numpy.linalg.eig.

#Determinante de matriz

det = np.linalg.det(matriz) 
#print(det)

valores, vectores= np.linalg.eig(matriz)
#print(vectores)


#%%

#d. Utilizando indexing obtenga un array unidimensional que contenga el elemento más cercano a 2.33 de cada fila. Repita para cada columna.

valor  = 2.33

def mas_cercano_fila(matrix):
    lista = []
    for i in range(0,matriz.shape[0]-1):
        
        x = matrix[i,:].flat[np.abs(matrix[i,:]- valor).argmin()]
        
        lista.append(x)
        
    return np.asarray(lista)

mascf = mas_cercano_fila(matriz)
print(mascf)

#%%

def mas_cercano_columna(matrix):
    lista = []
    for i in range(0,matriz.shape[1]-1):
        
        x = matrix[:,i].flat[np.abs(matrix[:,i]- valor).argmin()]
        
        lista.append(x)
        
    return np.asarray(lista)

mascc = mas_cercano_columna(matriz)
print(mascc)

#%%

###Ejercicio 2###

#a) Cree un array $x_{ij}$ distribuido normalmente (np.random.randn), con media $\mu_{i}$ = $i*10^{-2}$ y varianza $\sigma_{j}$ = $j*10^{-3}$, de dimensión 100×1000 (i es la fila, j es la columna).



x = 100 * (10**-2)


y = 1000 * (10**-3)

array = y*np.random.randn(100,1000)+x

print(array)
#%%
#b) Calcule la media por columna y la desviación estándar por fila. ¿Qué observa?

def media(matri):
    lista = []
    for i in range(0,matri.shape[1]-1):
        lista.append(np.median(matri[:,i]))
    return np.asarray(lista)

mediaa = media(array)
print(mediaa)
print(f'Media por columna : {mediaa}')

print(f'Media de todas las columnas : {np.median(mediaa)}')


def desvio(arra):
    lista1=[]
    for i in range(0,arra.shape[0]-1):
        lista1.append(np.std(arra[i,:]))
    return np.asarray(lista1)

desvioo = desvio(array)
print(f'Desvío estándar por fila: {desvioo}')
print(f'Desvío de todas las filas : {np.std(mediaa)}')





#%%
#c) Calcule el promedio por fila de los elementos que estén por encima de 0.7.

def promedio(arraa):
    lista2 = []
    for i in range(0, arraa.shape[0]-1):
        z = arraa.flat[np.where(arraa[i,:]>0.7)]
        lista2.append(np.mean(z))
    return np.asarray(lista2)

prom = promedio(array)
print(prom)


#Tip: Utilice np.where y, para el item c, un loop. Para el item a es posible hacer todo sin ningún loop.



