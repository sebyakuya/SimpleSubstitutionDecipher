#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys

if len(sys.argv)!=3:
	print "Error: faltan/sobran argumentos"
	exit()

esp = "EAOSRNIDLCTUMPBGVYQHFZJÑXKW"

try:
	frecuencias = open(sys.argv[2],"rb").readlines()
except:
	print "Error al leer fichero de frecuencias"
	exit()

frec_tmp = []
for f in frecuencias:
	frec_tmp.append(f.replace("\n","").replace("\r",""))
frecuencias = frec_tmp

frec = frecuencias[0].upper()
abc = frecuencias[1].upper()
dicc = zip(frec.upper(),abc.upper())

def texto(path):
	try:
		op = open(path,"rb")
		text = (op.read()).replace("\n","").replace("\r","") 
		return text.upper()
	except:
		print "Error al leer fichero de datos"
		exit()

def letraCorr(l):
	for tupla in dicc:
		if tupla[0]==l:
			return tupla[1]
		else:
			pass
	return l

palabra = texto(sys.argv[1])
print palabra + " -> "
print ""

plano = ""
for letra in palabra:
	plano=plano+letraCorr(letra)
print plano

print ""
print "FREC. TEXTO: "+frec
print "FREC. DICC:  "+abc