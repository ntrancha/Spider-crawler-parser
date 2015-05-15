#!/usr/bin/python2.7

import calendar
import datetime
import time
import urllib2
import os

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

def decoupe(string, start, size):
	index = 0
	ret = ""
	for lettre in string:
		if index >= start and size > 0:
			ret += lettre
			size-=1
		if size < 1:
			return ret
		index+=1
	return ret

def cut(string, delimiter, index):
	string.split
	for item in string.split(delimiter):
		if index == 0:
			return item
		index-=1
	return ""

def match(string, match):
	if match in string:
		return 1
	return 0

def mois_recup(string):
	strin = cut(string, " ", 2)
	if match(strin, "Jan"):
		return "1"
	if match(strin, "Feb"):
		return "2"
	if match(strin, "Mar"):
		return "3"
	if match(strin, "Apr"):
		return "4"
	if match(strin, "May"):
		return "5"
	if match(strin, "Jun"):
		return "6"
	if match(strin, "Jul"):
		return "7"
	if match(strin, "Aug"):
		return "8"
	if match(strin, "Sep"):
		return "9"
	if match(strin, "Oct"):
		return "10"
	if match(strin, "Nov"):
		return "11"
	if match(strin, "Dec"):
		return "12"

def is_number(string):
	for lettre in string:
		if lettre != "1" and lettre != "2" and lettre != "3" and lettre != "4":
			if lettre != "5" and lettre != "6" and lettre != "7":
				if lettre != "8" and lettre != "9" and lettre != "0":
					return 0
	return 1

def format_date(string):
	ret = string
	if is_number(string) == 1:
		if len(string) == 1:
			ret = "0" + string
	return ret

def jour_recup(string):
	format_date(cut(string, " ", 1))
	return cut(string, " ", 1)

def annee_recup(string):
	return cut(string, " ", 3)

def seconde_recup(string):
	return cut(cut(string, " ", 4), ":", 2)

def minute_recup(string):
	return cut(cut(string, " ", 4), ":", 1)

def heure_recup(string):
	return cut(cut(string, " ", 4), ":", 0)

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
			balise = cut(ligne, ">", 0)
			body = cut(ligne, ">", 1)
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
				image = cut(balise, '"', 1)
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
			duree = cut(ligne, '>', 1)
		if match(ligne, "yt-uix-tile-link") == 1 and match(ligne, "watch?v="):
			lien = cut(ligne, '"', 11)
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
			titre = cut(ligne, '"', 7)
			url0 = cut(url, '=', 1)
			frame = '<iframe width="853" height="480" src="https://www.youtube.com/embed/'+url0+'" frameborder="0" allowfullscreen></iframe>'
			chaine = str(timestamp) +de+ rssid +de+ titre +de+ date +de+ url +de+ frame
			liste.append(chaine)
                        #add_vgs(titre, date, url, frame)
		if match(ligne, "datePublished") == 1:
			date =  cut(ligne, '"', 3)
			date0 = datetime.datetime.strptime(date, "%Y-%m-%d")
			timestamp = calendar.timegm(date0.utctimetuple())

def dcp(x, y, buttom, wait):
    deplace(x, y)
    clic(buttom)
    paus(wait)

def copier_texte(string):
    ecrire("copy.txt", string)
    execute("gedit copy.txt &")
    paus(1)
    execute('wmctrl -r "gedit" -e 0,1900,0,1000,1000 2>/dev/null')
    execute('wmctrl - a "gedit" 2>/dev/null')
    dcp(2331, 259, 1, 1)
    execute('xdotool keydown Ctrl')
    paus(1)
    execute('xdotool key a')
    paus(1)
    execute('xdotool key c')
    paus(1)
    execute('xdotool keyup Ctrl')

def str_replace(string):
    ret = str(string)
    retu = ret.replace("&#39;", "'")
    ret = retu.replace("&quot;", '"')
    return ret

def sav_article(liste):
    while len(liste) > 0:
        val = liste[0]
        tim = cut(val, "++q++", 0)
        titre0 = cut(val, "++q++", 2)
        titre = str_replace(titre0)
        date = cut(val, "++q++", 3)
        url = cut(val, "++q++", 4)
        frame = cut(val, "++q++", 5)
        print titre
        add_vgs(titre, date, url, frame)
        liste.remove(val)

def add_vgs(titre, date, url, frame):
    execute('xdotool keydown Ctrl')
    execute('xdotool keyup Ctrl')
    #clique jommla
    #dcp(156, 196, 1, 3)
    dcp(210, 127, 1, 1)
    dcp(209, 317, 1, 1)
    while test_url("Administration - Panneau d'administration") == 0:
        dcp(210, 127, 1, 1)
        dcp(209, 317, 1, 1)
        paus(2)
    #ajouter un article
    dcp(1303, 298, 1, 2)
    if test_url("Gestion des articles : Ajouter un article") == 0:
        add_vgs(titre, date, url, frame)
    #titre
    copier_texte(titre)
    ##titre
    dcp(72, 345, 1, 1)
    execute('xdotool keydown Ctrl')
    paus(1)
    execute('xdotool key v')
    paus(1)
    execute('xdotool keyup Ctrl')
    execute('killall "gedit"')
    #frame
    dcp(82, 674, 1, 1)
    copier_texte(frame)
    ##php
    dcp(165, 358, 1, 1)
    execute('xdotool keydown Ctrl')
    paus(1)
    execute('xdotool key v')
    paus(1)
    execute('xdotool keyup Ctrl')
    execute('killall "gedit"')
    paus(1)
    ##inserer
    dcp(114, 265, 1, 1)
    ##categorie
    dcp(512, 355, 1, 1)
    execute('xdotool key V')
    paus(1)
    ##video
    dcp(457, 403, 1, 1)
    ##date
    dcp(250, 296, 1, 1)
    date0 = date +  " 00:00:00"
    ecrire("copy.txt", date0)
    execute("gedit copy.txt &")
    paus(2)
    execute('wmctrl -r "gedit" -e 0,1900,0,1000,1000 2>/dev/null')
    execute('wmctrl - a "gedit" 2>/dev/null')
    ##gedit
    dcp(2331, 259, 1, 1)
    execute('xdotool keydown Ctrl')
    paus(1)
    execute('xdotool key a')
    paus(1)
    execute('xdotool key c')
    paus(1)
    execute('xdotool keyup Ctrl')
    paus(1)
    dcp(210, 534, 1, 1)
    execute('xdotool keydown Ctrl')
    paus(1)
    execute('xdotool key v')
    paus(1)
    dcp(980, 348, 1, 1)
    execute('xdotool key v')
    paus(1)
    execute('xdotool keyup Ctrl')
    execute('killall "gedit"')
    paus(1)
    ##enregistrer
    dcp(130, 250, 1, 1)

def test_url(string):
    paus(1)
    com = commande("wmctrl -l | grep Mozilla")
    if match(com, string) == 0:
        return 0
    return 1

def deplace(x, y):
    commande = "xdotool mousemove " + str(x) + " " + str(y)
    execute(commande)

def clic(buttom):
    commande = "xdotool click " + str(buttom)
    execute(commande)

def clavier(string):
    commande = 'xdotool type "' + string  + '"'
    execute(commande)

def timestamp():
    return time.time()

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

if __name__=='__main__':
	liste = []
	mon_fichier = open("b.txt", "r")
	contenu = mon_fichier.readlines()
	mon_fichier.close()
	for line in contenu:
		ligne = decoupe(line, 0, len(line) - 1)
		rssid = cut(ligne, ";", 0)
		url = cut(ligne, ";", 1)
		if match(url, "youtube") == 1:
			youtube(url, liste, rssid)
		#else
			#crawler(url, liste, rssid)
                #break
	liste.sort(reverse=True)
        sav_article(liste)
	print liste
