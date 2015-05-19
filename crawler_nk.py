#!/usr/bin/python2.7

import string_nk
import control_nk
import spider_nk
import system_nk
import date_nk
import urllib2
import calendar
import datetime

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
		if string_nk.decoupe(ligne, 0, 1) != '/':
			balise = string_nk.cut(ligne, ">", 0)
			body = string_nk.cut(ligne, ">", 1)
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
				jour = date_nk.format_date(date_nk.jour_recup(date))
				mois = date_nk.format_date(date_nk.mois_recup(date))
				annee = date_nk.annee_recup(date)
				seconde = date_nk.format_date(date_nk.seconde_recup(date))
				minute = date_nk.format_date(date_nk.minute_recup(date))
				heure = date_nk.format_date(date_nk.heure_recup(date))
				date1 = annee + mois + jour + " " + heure + ":" + minute + ":" + seconde
				date0 = datetime.datetime.strptime(date1, "%Y%m%d %H:%M:%S")
				timestamp = calendar.timegm(date0.utctimetuple())
			elif string_nk.match(balise, "link"):
				lien = body
			elif string_nk.match(balise, "enclosure") and string_nk.match(balise,"url="):
				image = string_nk.cut(balise, '"', 1)
			else:
				if etat == 1:
					etat = 0
					chaine = str(timestamp) +de+ rssid +de+ titre +de+ description +de+ lien +de+ image
					liste.append(chaine)

def test_titre2(titre):
	test = system_nk.commande('grep "'+string_nk.str_replace2(titre)+'" sav.nk | wc -l')
	if int(test) == 0:
		print "\033[1m\033[92mNew topic\033[0m"
		return 1
	else:
		print "\033[1m\033[91mTopic exist\033[0m"
		return 0

def test_titre(titre, test):
	test += 1
	if test == 1:
		print "\033[94m  Testing Double topics"
	control_nk.dcp(196, 110, 1, 2)								  	# VGS #
	control_nk.dcp(226, 304, 1, 6)								  	# ADMIN #
	if control_nk.test_url2("Administration - Panneau d'administration") == 0:
		return test_titre(titre, test)
	control_nk.dcp(1138, 314, 1, 6)							   		# Gestion articles #
	if control_nk.test_url2("Administration - Gestion des articles") == 0:
		return test_titre(titre, test)
	control_nk.dcp(544, 289, 1, 6)							   		# Effacer #
	if control_nk.test_url2("Administration - Gestion des articles") == 0:
		return test_titre(titre, test)
	control_nk.ddcp(271, 290, 1, 2)							   		# Rechercher #
	control_nk.copier(titre)
	control_nk.ctrl_V()
	control_nk.dcp(505, 289, 1, 6)							   		# Recherche #
	if control_nk.test_url2("Administration - Gestion des articles") == 0:
		return test_titre(titre, test)
	control_nk.ddcp(972, 368, 1, 2)							   		# Public #
	control_nk.ctrl_C()
	test = control_nk.xclip()
	if string_nk.match(test, "Public") == 1:
		print "\033[1m\033[91mTopic exist\033[0m"
		if int(system_nk.commande('grep "'+titre+'" sav.nk | wc -l')) == 0:
			print "\033[93mAdd topic"
			commande = 'echo "' + string_nk.str_replace2(titre) + '" >> sav.nk'
 			system_nk.execute(commande)
		return 0
	return 1

def youtube(url, liste, rssid, count, cat):
	page0 = str(download(url))
	page = page0.replace('\n', '')
	page.split
	compteur = 0
	for ligne in page.split("<"):
		if string_nk.match(ligne, "minutes") == 1:
			duree = string_nk.cut(ligne, '>', 1)
		if string_nk.match(ligne, "yt-uix-tile-link") == 1 and string_nk.match(ligne, "watch?v="):
			lien = string_nk.cut(ligne, '"', 11)
			lien = "https://www.youtube.com" + lien
			compteur += 1
			print "\033[95m=================================================================================="
			print "\033[94m  Crawling ...\t\t[\033[92m\033[1m" + str(compteur)  + "\033[0m\033[94m]"
			if crawler_youtube(lien, liste, rssid, cat) == 0:
				#break
				a = 1
		if string_nk.match(ligne, "yt-uix-button-content") == 1 and string_nk.match(ligne, "Plus"):
			break

def crawler_youtube(url, liste, rssid, cat):
	de = "++q++"
	page0 = str(download(url))
	page = page0.replace('\n', '')
	page.split
	for ligne in page.split("<"):
		if string_nk.match(ligne, "watch-title") == 1 and string_nk.match(ligne, "eow-title") == 1:
			titre = string_nk.str_replace(string_nk.cut(ligne, '"', 7))
			print "\033[0m\033[93mChannel  \t\033[94m=> \t\033[1m\033[97m" + rssid
			print "\033[0m\033[93mCategory \t\033[94m=> \t\033[1m\033[97m" + cat
			print "\033[0m\033[93mVideo    \t\033[94m=> \t\033[1m\033[97m" + titre + "\033[0m\033[94m"
			if test_titre2(titre) == 0:
				return 0
				break
			if test_titre(titre, 0) == 0:
				return 0
				break
			url0 = string_nk.cut(url, '=', 1)
			frame = '<iframe width="853" height="480" src="https://www.youtube.com/embed/'+url0+'" frameborder="0" allowfullscreen></iframe>'
			chaine = str(timestamp) +de+ rssid +de+ titre +de+ date +de+ cat +de+ frame
			liste.append(chaine)
			spider_nk.sav_article(liste, 0)
		if string_nk.match(ligne, "datePublished") == 1:
			date =  string_nk.cut(ligne, '"', 3)
			date0 = datetime.datetime.strptime(date, "%Y-%m-%d")
			timestamp = calendar.timegm(date0.utctimetuple())
	return 1

