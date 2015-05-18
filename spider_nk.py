#!/usr/bin/python2.7

import os
import string_nk
import crawler_nk
import article_nk

def sav_article(liste, test):
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
		article_nk.articles(titre, date, url, frame, chaine, liste, test)

def recup_liste(fichier, liste, num, maxi):
	count = 0
	mon_fichier = open(fichier, "r")
	contenu = mon_fichier.readlines()
	mon_fichier.close()
	print "\033[94mLecture du fichier [\033[93m\033[1m" + fichier  + "\033[0m\033[94m]"
	print "\033[95m\033[1m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m\033[94m"
	for line in contenu:
		ligne = string_nk.decoupe(line, 0, len(line) - 1)
		chaine = string_nk.cut(ligne, ";", 0)
		url = string_nk.cut(ligne, ";", 1)
		cat = string_nk.cut(ligne, ";", 2)
		if string_nk.match(url, "youtube") == 1:
			count += 1
			if count >= int(num):
				print "Chaine Youtube [\033[92m\033[1m" + chaine + "\033[0m\033[94m] (n_\033[92m" + str(count) + "\033[94m)"
				crawler_nk.youtube(url, liste, chaine, count, cat)
				print "\033[95m\033[1m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m\033[94m"
				if count == int(num) + int(maxi):
					break
		#else
			#crawler_nk.crawler(url, liste, rssid)
	return liste

def spider(num, maxi):
	liste = []
	recup_liste("flux.nk", liste, num, maxi)
	liste.sort(reverse=True)
