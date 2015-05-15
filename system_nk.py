#!/usr/bin/python2.7

import os

def contenue(fichier):
    try:
        mon_fichier = open(fichier, "r")
        f_contenu = mon_fichier.read()
        mon_fichier.close()
    except:
        print "Error open:"+ fichier
        return 1
    return f_contenu

def commande(ordre):
    com = "{0} > tempo.txt".format(ordre)
    execute(com)
    cont = contenue('tempo.txt')
    delete('tempo.txt')
    return cont

def paus(time):
    com = "sleep " + str(time)
    execute(com)
    return 1

def execute(ordre):
    try:
        os.system(ordre)
    except:
        return 0
    return 1

def delete(fichier):
    try:
        os.remove(fichier)
    except:
        return 0
    return 1

def ecrire(fichier, string):
    commande = 'echo "' + string + '" > ' + fichier
    execute(commande)
