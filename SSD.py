#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys

print """
##############################################################
# Alvaro Reyes - Simple Sustitution Decipher                 #
##############################################################
# python SSD.py cipher.txt frequency.txt                     #
##############################################################
"""

if len(sys.argv) is 1:
	print "Howto: enter ciphertext and frequency file and you will get the translation"
	print "Frequency file must have only two lines: frequency of ciphertext and frequency of language"
	print "Example of frequency file:"
	print "THBONKFREGJVUMIYDALCSQWZPX  <- Frequency of ciphertext"
	print "EAORSNITUCMDLPGQBYVAZFJXKW  <- Frequency of language" 
	print "You can use the frequencyanalyzer.py to get the frequency file"
	exit()

if len(sys.argv)!=3:
	print "Error: incorrect no. of arguments"
	print "Correct input is: cipher.txt frequency.txt"
	exit()

try:
	frequencies = open(sys.argv[2],"rb").readlines()
except:
	print "Failed to read frequency file"
	exit()

frec_tmp = []
for f in frequencies:
	frec_tmp.append(f.replace("\n","").replace("\r",""))
frequencies = frec_tmp

frec = frequencies[0].upper()
abc = frequencies[1].upper()
dicc = zip(frec.upper(),abc.upper())

def getCipherText(path):
	try:
		op = open(path,"rb")
		text = (op.read()).replace("\n","").replace("\r","") 
		return text.upper()
	except:
		print "Failed to read cipher text"
		exit()

def fixedChar(l):
	for tupla in dicc:
		if tupla[0]==l:
			return tupla[1]
		else:
			pass
	return l

word = getCipherText(sys.argv[1])
print word + " -> "
print ""

plaintext = ""
for char in word:
	plaintext=plaintext+fixedChar(char)
print plaintext

print ""
print "Text. freq. "+frec
print "Dicc. freq.:  "+abc