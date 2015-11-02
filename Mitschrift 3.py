# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:27:25 2015

@author: jakobunfried
"""


"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%    Vergleich von Objekten    %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
print
print
print "# Vergleich von Objekten"
print

a = 42
b = 43

if a is b:
    print("a und b verweisen auf das selbe Objekt mit dem selben physischen Speicherbereich")
if a == b:
    print("a und b haben den gleichen Wert")
if type(a) is type(b):
    print("a und b sind vom gleichen Typ")
    
    
    
"""
%%%%%%%%%%%%%%%%%%%%%%%
%%%    Schleifen    %%%
%%%%%%%%%%%%%%%%%%%%%%%
"""
print 
print
print "# Schleifen"
print
#mehr Beispiele siehe Test.py , Eulerverfahren.py

""" for Schleife, für schon bekannte Anzahl an Iterationen """

for i in [1,2,3]:
    print "Zahl ",i
for i in range(0,10):
    print i,
print
for i in "Hallo":
    print "Buchstabe",i
for i in ("a",a,42, [1,2,3],"Hallo"):
    print "Tupelelement ", i
    
""" while Schleife, Iteration bis Bedingung erfüllt ist """

a = 2048; a_orig = a; exp = 0;
while a>1:
    a /= 2
    exp += 1
print a_orig, "=", 2, "^", exp    

#NICHT machen:  while True:
    
""" Kontrollstrukturen in Schleifen """
# continue bricht aktuellen Durchlauf ab und startet nächsten
# break bricht die Schleife ab

a = ("let","us","find","Bilbo","again")
for word in a:
    if word == "Bilbo":
        print "found Bilbo."
        break
print word

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%    "Hausaufgabe"    %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

#Folien 62,63,64 Heun Verfahren implementieren

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%    Methoden def     %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
print 
print
print "# Methoden def"
print

def hi():
    print("Hello World")
hi()
a = hi()
print type(a)

h = hi
h()
print type(h)
    