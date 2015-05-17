#!/usr/bin/python2.7

import os
import string_nk
import crawler_nk
import article_nk

def sav_article(liste):
	while len(liste) > 0:
		val = liste[0]
		tim = string_nk.cut(val, "++q++", 0)
		chaine = string_nk.cut(val, "++q++", 1)
		titre0 = string_nk.cut(val, "++q++", 2)
		titre = string_nk.str_replace(titre0)
		date = string_nk.cut(val, "++q++", 3)
		url = string_nk.cut(val, "++q++", 4)
		frame = string_nk.cut(val, "++q++", 5)
		#add_vgs(titre, date, url, frame)
		article_nk.articles(titre, date, url, frame, chaine)
		liste.remove(val)

def recup_liste(fichier, liste):
	count = 0
	mon_fichier = open(fichier, "r")
	contenu = mon_fichier.readlines()
	mon_fichier.close()
	print "Lecture du fichier [" + fichier  + "]"
	for line in contenu:
		ligne = string_nk.decoupe(line, 0, len(line) - 1)
		chaine = string_nk.cut(ligne, ";", 0)
		url = string_nk.cut(ligne, ";", 1)
		cat = string_nk.cut(ligne, ";", 2)
		if string_nk.match(url, "youtube") == 1:
			print "Chaine Youtube [" + chaine + "]"
			crawler_nk.youtube(url, liste, chaine, count, cat)
		#else
			#crawler_nk.crawler(url, liste, rssid)
	return liste

def spider():
	liste = []
	recup_liste("flux.nk", liste)
	liste.sort(reverse=True)
