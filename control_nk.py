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
    system_nk.execute(commande) uuu

def dcp(x, y, buttom, wait):
    deplace(x, y)
    clic(buttom)
    system_nk.paus(wait)

def copier(string):
    commande='echo "' + string + '" | xclip -i'
    system_nk.execute("commande")
