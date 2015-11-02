# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:36:39 2015

@author: jakobunfried
"""

#Berechnen des Produkts aller Einträge eines Tupels
print
a = 1
t = (3,7,6,2) 
for i in (3,7,6,2):
    a *= i
print "Produkt aller Einträge des Tupels", t , "ergibt" , a

#Skalarprodukt zweier Vektoren
print
v = (2,1,3,2)
print "v =", v
w = (1,4,3,2)
print "w =", w
prod = 0
for i in range (0,4):
    prod += w[i] * v[i]
print "Skalarprodukt v * w =",prod