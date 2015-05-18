#!/usr/bin/python2.7

import system_nk
import string_nk

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
	system_nk.paus(wait)

def ddcp(x, y, buttom, wait):
	deplace(x, y)
	clic(buttom)
	clic(buttom)
	system_nk.paus(wait)

def copier(string):
	com = 'echo "' + string + '" | xsel -b'
	system_nk.execute(com)

def ctrl_A():
	ctrl("a")
	system_nk.paus(1)

def ctrl_C():
	ctrl("c")
	system_nk.paus(1)

def ctrl_V():
	ctrl("v")
	system_nk.paus(1)

def xclip():
	com = 'xsel -b'
	return system_nk.commande(com)

def init_ctrl():
	system_nk.execute('xdotool keydown Ctrl')
	system_nk.execute('xdotool keyup Ctrl')

def enter():
	system_nk.execute('xdotool key KP_Enter')

def ctrl(lettre):
	system_nk.execute('xdotool keydown Ctrl')
	system_nk.paus(1)
	commande = "xdotool key " + lettre
	system_nk.execute(commande)
	system_nk.paus(1)
	system_nk.execute('xdotool keyup Ctrl')
	system_nk.paus(1)

def test_url(string):
	system_nk.paus(1)
	com = system_nk.commande("wmctrl -l | grep Mozilla")
	if string_nk.match(com, string) == 0:
		print "\033[0m\033[91m<Disconnect>\033[0m"
		return 0
	return 1

def test_url2(string):
	system_nk.paus(1)
	com = system_nk.commande("wmctrl -l | grep Mozilla")
	if string_nk.match(com, string) == 0:
		return 0
	return 1
