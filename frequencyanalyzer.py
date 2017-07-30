#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from operator import itemgetter

print """
##############################################################
# Alvaro Reyes - Frequency analyzer                          #
##############################################################
# python frequencyanalyzer.py archivo language               #
# Language can be spanish, spanyish or english               #
##############################################################
"""

if len(sys.argv) is 1:
	print "Howto: enter file to be analyzed and optionally the language you want to compare"
	print "It returns a two-lined file with the frequency of the text and the frequency of the language"
	exit()

try:
	texto = open(sys.argv[1],'r')
except:
	print "Failed to read file"
	exit()

dicc = []

try:
	# Para cada linea del fichero
	for linea in texto:
		# Pasamos a mayusculas 
		linea = linea.upper()

		# Para cada letra de la linea
		for i in range(0,len(linea)):
			letra = linea[i]

			# Si la letra es una letra como tal
			if letra in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
				# Comprobamos si ya existe en el array de keys
				keys = [x[0] for x in dicc]

				if letra in keys:
					# Si ya esta, se añade 1 mas a la letra correspondiente
					dicc[keys.index(letra)][1] += 1
				else:
					# Si no esta, se añade una nueva entrada
					dicc.append([letra,1])
except:
	print "I'm sorry, but I'm not prepared for this kind of text"
	texto.close()
	exit()

texto.close()

# Lista inversa del diccionario ordenado empezando las ocurrencias y luego por orden alfabetico

keys = [x[0] for x in list(reversed(sorted(dicc, key=itemgetter(1,0))))]

print "".join(keys)
frec = "".join(keys)

language =""
try:
	if len(sys.argv) is 3:
		p = sys.argv[2] 

		if p == "spanish":
			language = "EAORSNITUCMDLPGQBYVAZFJXKW"
		elif p == "spanyish":
			language = "EAORSNITUCMDLPGQBYVAZFJÑXKW"
		elif p == "english":
			language = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
		else:
			print "Language not registered"
except:
	print "Failed to show language frequency"	


output = open("output.txt","w")
output.write(frec+"\n")
output.write(language)
output.close()