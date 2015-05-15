#!/usr/bin/python2.7

import calendar
import datetime
import time
import urllib2
import os
import string_nk
import system_nk
import date_nk
import control_nk
import crawler_nk

def copier_texte(string):
    system_nk.ecrire("copy.txt", string)
    system_nk.execute("gedit copy.txt &")
    system_nk.paus(1)
    system_nk.execute('wmctrl -r "gedit" -e 0,1900,0,1000,1000 2>/dev/null')
    system_nk.execute('wmctrl - a "gedit" 2>/dev/null')
    dcp(2331, 259, 1, 1)
    system_nk.execute('xdotool keydown Ctrl')
    system_nk.paus(1)
    system_nk.execute('xdotool key a')
    system_nk.paus(1)
    system_nk.execute('xdotool key c')
    system_nk.paus(1)
    system_nk.execute('xdotool keyup Ctrl')

def str_replace(string):
    ret = str(string)
    retu = ret.replace("&#39;", "'")
    ret = retu.replace("&quot;", '"')
    return ret

def sav_article(liste):
    while len(liste) > 0:
        val = liste[0]
        tim = string_nk.cut(val, "++q++", 0)
        titre0 = string_nk.cut(val, "++q++", 2)
        titre = str_replace(titre0)
        date = string_nk.cut(val, "++q++", 3)
        url = string_nk.cut(val, "++q++", 4)
        frame = string_nk.cut(val, "++q++", 5)
        print titre
        add_vgs(titre, date, url, frame)
        liste.remove(val)

def add_vgs(titre, date, url, frame):
    system_nk.execute('xdotool keydown Ctrl')
    system_nk.execute('xdotool keyup Ctrl')
    #clique jommla
    #dcp(156, 196, 1, 3)
    dcp(210, 127, 1, 1)
    dcp(209, 317, 1, 1)
    while test_url("Administration - Panneau d'administration") == 0:
        dcp(210, 127, 1, 1)
        dcp(209, 317, 1, 1)
        system_nk.paus(2)
    #ajouter un article
    dcp(1303, 298, 1, 2)
    if test_url("Gestion des articles : Ajouter un article") == 0:
        add_vgs(titre, date, url, frame)
    #titre
    copier_texte(titre)
    ##titre
    dcp(72, 345, 1, 1)
    system_nk.execute('xdotool keydown Ctrl')
    system_nk.paus(1)
    system_nk.execute('xdotool key v')
    system_nk.paus(1)
    system_nk.execute('xdotool keyup Ctrl')
    system_nk.execute('killall "gedit"')
    #frame
    dcp(82, 674, 1, 1)
    copier_texte(frame)
    ##php
    dcp(165, 358, 1, 1)
    system_nk.execute('xdotool keydown Ctrl')
    system_nk.paus(1)
    system_nk.execute('xdotool key v')
    system_nk.paus(1)
    system_nk.execute('xdotool keyup Ctrl')
    system_nk.execute('killall "gedit"')
    system_nk.paus(1)
    ##inserer
    dcp(114, 265, 1, 1)
    ##categorie
    dcp(512, 355, 1, 1)
    system_nk.execute('xdotool key V')
    system_nk.paus(1)
    ##video
    dcp(457, 403, 1, 1)
    ##date
    dcp(250, 296, 1, 1)
    date0 = date +  " 00:00:00"
    system_nk.ecrire("copy.txt", date0)
    system_nk.execute("gedit copy.txt &")
    system_nk.paus(2)
    system_nk.execute('wmctrl -r "gedit" -e 0,1900,0,1000,1000 2>/dev/null')
    system_nk.execute('wmctrl - a "gedit" 2>/dev/null')
    ##gedit
    dcp(2331, 259, 1, 1)
    system_nk.execute('xdotool keydown Ctrl')
    system_nk.paus(1)
    system_nk.execute('xdotool key a')
    system_nk.paus(1)
    system_nk.execute('xdotool key c')
    system_nk.paus(1)
    system_nk.execute('xdotool keyup Ctrl')
    system_nk.paus(1)
    dcp(210, 534, 1, 1)
    system_nk.execute('xdotool keydown Ctrl')
    system_nk.paus(1)
    system_nk.execute('xdotool key v')
    system_nk.paus(1)
    dcp(980, 348, 1, 1)
    system_nk.execute('xdotool key v')
    system_nk.paus(1)
    system_nk.execute('xdotool keyup Ctrl')
    system_nk.execute('killall "gedit"')
    system_nk.paus(1)
    ##enregistrer
    dcp(130, 250, 1, 1)

def test_url(string):
    system_nk.paus(1)
    com = commande("wmctrl -l | grep Mozilla")
    if string_nk.match(com, string) == 0:
        return 0
    return 1

def timestamp():
    return time.time()

if __name__=='__main__':
	liste = []
	mon_fichier = open("b.txt", "r")
	contenu = mon_fichier.readlines()
	mon_fichier.close()
	for line in contenu:
		ligne = string_nk.decoupe(line, 0, len(line) - 1)
		rssid = string_nk.cut(ligne, ";", 0)
		url = string_nk.cut(ligne, ";", 1)
		if string_nk.match(url, "youtube") == 1:
			crawler_nk.youtube(url, liste, rssid)
		#else
			#crawler_nk.crawler(url, liste, rssid)
                #break
	liste.sort(reverse=True)
        #sav_article(liste)
	print liste
