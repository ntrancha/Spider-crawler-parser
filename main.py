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

def download(url):
	attempts = 0
	while attempts < 3:
	    try:
	        response = urllib2.urlopen(url, timeout = 5)
	        content = response.read()
                return content
	    except urllib2.URLError as e:
	        attempts += 1
	        print type(e)

def crawler(url, liste, rssid):
	page0 = str(download(url))
	page = page0.replace('\n', '')
	page.split
	titre = ""
	description = ""
	date = ""
	seconde = ""
	minute = ""
	heure = ""
	jour = ""
	mois = ""
	annee = ""
	lien = ""
	image = ""	
	etat = 0
	de = "++q++"
	for ligne in page.split("<"):
		#print ligne
		if decoupe(ligne, 0, 1) != '/':
			balise = system_nk.cut(ligne, ">", 0)
			body = system_nk.cut(ligne, ">", 1)
			#if balise == "item":
				#etat = 1
			if balise == "title":
				titre = body
			elif balise == "description":
				description = body
				if len(description) > 0:
					etat = 1
				else:
					etat = 0
			elif balise == "pubDate":
				date = body
				jour = format_date(jour_recup(date))
				mois = format_date(mois_recup(date))
				annee = annee_recup(date)
				seconde = format_date(seconde_recup(date))
				minute = format_date(minute_recup(date))
				heure = format_date(heure_recup(date))
				date1 = annee + mois + jour + " " + heure + ":" + minute + ":" + seconde
				date0 = datetime.datetime.strptime(date1, "%Y%m%d %H:%M:%S")
				timestamp = calendar.timegm(date0.utctimetuple())
			elif match(balise, "link"):
				lien = body
			elif match(balise, "enclosure") and match(balise,"url="):
				image = system_nk.cut(balise, '"', 1)
			else:
				if etat == 1:
					etat = 0
					chaine = str(timestamp) +de+ rssid +de+ titre +de+ description +de+ lien +de+ image
					liste.append(chaine)

def youtube(url, liste, rssid):
	page0 = str(download(url))
	page = page0.replace('\n', '')
	page.split
	for ligne in page.split("<"):
		if match(ligne, "minutes") == 1:
			duree = system_nk.cut(ligne, '>', 1)
		if match(ligne, "yt-uix-tile-link") == 1 and match(ligne, "watch?v="):
			lien = system_nk.cut(ligne, '"', 11)
			lien = "https://www.youtube.com" + lien
			crawler_youtube(lien, liste, rssid)
		if match(ligne, "yt-uix-button-content") == 1 and match(ligne, "Plus"):
			break

def crawler_youtube(url, liste, rssid):
	de = "++q++"
	page0 = str(download(url))
	page = page0.replace('\n', '')
	page.split
	for ligne in page.split("<"):
		if match(ligne, "watch-title") == 1 and match(ligne, "eow-title") == 1:
			titre = system_nk.cut(ligne, '"', 7)
			url0 = system_nk.cut(url, '=', 1)
			frame = '<iframe width="853" height="480" src="https://www.youtube.com/embed/'+url0+'" frameborder="0" allowfullscreen></iframe>'
			chaine = str(timestamp) +de+ rssid +de+ titre +de+ date +de+ url +de+ frame
			liste.append(chaine)
                        #add_vgs(titre, date, url, frame)
		if match(ligne, "datePublished") == 1:
			date =  system_nk.cut(ligne, '"', 3)
			date0 = datetime.datetime.strptime(date, "%Y-%m-%d")
			timestamp = calendar.timegm(date0.utctimetuple())

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
        tim = system_nk.cut(val, "++q++", 0)
        titre0 = system_nk.cut(val, "++q++", 2)
        titre = str_replace(titre0)
        date = system_nk.cut(val, "++q++", 3)
        url = system_nk.cut(val, "++q++", 4)
        frame = system_nk.cut(val, "++q++", 5)
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
    if match(com, string) == 0:
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
		ligne = decoupe(line, 0, len(line) - 1)
		rssid = system_nk.cut(ligne, ";", 0)
		url = system_nk.cut(ligne, ";", 1)
		if match(url, "youtube") == 1:
			youtube(url, liste, rssid)
		#else
			#crawler(url, liste, rssid)
                #break
	liste.sort(reverse=True)
        sav_article(liste)
	print liste
