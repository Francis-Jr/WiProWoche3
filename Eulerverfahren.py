# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:14:47 2015

@author: jakobunfried
"""

""" Numerische Lösung von DGLs """
""" explizites Eulerverfahren """

# DGL =  p'(t) = f(t,p(t))
# Vorwärtdifferenz p'(t) ~ (p(t+dt) - p(t)) / dt
# hier logistische DGL: p'(t) = a*p(t) - b*p(t)^2
# Iterationsvorschrift:  p(t+dt) = p(t) + dt * (a*p(t) - b * p(t)^2)

a = 1. # Parameter
b = 0.01
p0 = 10. #Anfangswert
tend = 3. # Interv [0,tend]
N = 6 # Teilintervalle
dt = tend/N
p = p0
t= 0

for i in range (0,N+1):
    t = t + dt
    p = p + dt*(a*p - b*(p**2))
    print "%6d %7.3f" % (t,p)