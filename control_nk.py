#!/usr/bin/python2.7

import system_nk

def deplace(x, y):
	commande = "xdotool mousemove " + str(x) + " " + str(y)
	system_nk.execute(commande)

def clic(buttom):
	commande = "xdotool click " + str(buttom)
	system_nk.execute(commande)
	
def clavier(string):
	commande = 'xdotool type "' + string  + '"'
	system_nk.execute(commande)

def dcp(x, y, buttom, wait):
	deplace(x, y)
	clic(buttom)
	clic(buttom)
	system_nk.paus(wait)

def ddcp(x, y, buttom, wait):
	deplace(x, y)
	clic(buttom)
	system_nk.paus(wait)

def copier(string):
	com = 'echo "' + string + '" | xsel -b'
	system_nk.execute(com)

def xclip():
	com = 'xsel -b'
	return system_nk.commande(com)

def init_ctrl():
	system_nk.execute('xdotool keydown Ctrl')
	system_nk.execute('xdotool keyup Ctrl')

def ctrl(lettre):
	system_nk.execute('xdotool keydown Ctrl')
	system_nk.paus(1)
	commande = "xdotool key " + lettre
	system_nk.execute('xdotool key v')
	system_nk.paus(1)
	system_nk.execute('xdotool keyup Ctrl')
