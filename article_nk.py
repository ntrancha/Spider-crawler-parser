#!/usr/bin/python2.7

import control_nk
import spider_nk
import crawler_nk
import system_nk

def admin(titre, date, url, frame, chaine, liste, test):
	control_nk.dcp(196, 110, 1, 2)									# VGS #
	control_nk.dcp(226, 304, 1, 6)									# ADMIN #
	if control_nk.test_url("Administration - Panneau d'administration") == 0:
		articles(titre, date, url, frame, chaine, liste, test)
	else:
		add_article(titre, date, url, frame, chaine, liste, test)

def add_article(titre, date, url, frame, chaine, liste, test):
	control_nk.dcp(1126, 285, 1, 6)									# nouvel article #
	if control_nk.test_url("Administration") == 0:
		articles(titre, date, url, frame, chaine, liste, test)
	else:
		add_titre(titre, date, url, frame, chaine, liste, test)

def add_titre(titre, date, url, frame, chaine, liste, test):
	control_nk.dcp(173, 333, 1, 2)									# titre #
	title = "[" + chaine + "] " + titre
	control_nk.copier(title)
	control_nk.ctrl_V()
	categorie(titre, date, url, frame, chaine, liste, test)

def categorie(titre, date, cat, frame, chaine, liste, test):
	control_nk.dcp(577, 342, 1, 2)									# Categorie #
	control_nk.copier(cat)
	control_nk.ctrl_V()
	control_nk.dcp(463, 396, 1, 2)									# Video #
	frame2(titre, date, cat, frame, chaine, liste, test)

def frame2(titre, date, url, frame, chaine, liste, test):
	control_nk.dcp(77, 663, 1, 6)									# inserer le code #
	control_nk.copier(frame)
	control_nk.dcp(175, 357, 1, 2)									# HTML #
	control_nk.ctrl_V()
	control_nk.dcp(173, 249, 1, 6)									# inserer #
	param(titre, date, url, frame, chaine, liste, test)

def param(titre, date, url, frame, chaine, liste, test):
	control_nk.dcp(252, 285, 1, 6)									# parametre article #
	control_nk.dcp(217, 516, 1, 2)									# date de creation #
	date0 = date +  " 00:00:00"
	control_nk.copier(date0)
	control_nk.ctrl_V()
	control_nk.dcp(850, 332, 1, 2)									# date de pub #
	control_nk.copier(date0)
	control_nk.ctrl_V()
	enregistrer(titre, date, url ,frame, chaine, liste, test)

def enregistrer(titre, date, url, frame, chaine, liste, test):
	control_nk.dcp(149, 232, 1, 8)									# enregistrer #
	test = system_nk.commande('grep "'+titre+'" sav.nk | wc -l')
	if control_nk.test_url("Modifier") == 0:		# Mauvaise page
		if test == 0:								# 2eme test
			if crawler_nk.test_titre(titre, 0) == 0:	# Mauvaise page
				print "\033[1m\033[91mError (topic)\033[0m"
				spider_nk.sav_article(liste, test)
				if int(test) == 0:
					commande = 'echo "' + titre + '" >> sav.nk'
					system_nk.execute(commande)
			else:									# Bonne page
				print "\033[1m\033[92mTopic added\033[0m"
				val = liste[0]
				liste.remove(val)
				if int(test) == 0:
					commande = 'echo "' + titre + '" >> sav.nk'
					system_nk.execute(commande)
		else:										# Rate
			print "\033[1m\033[91mError (topic) 2\033[0m"
			val = liste[0]
			liste.remove(val)
			if int(test) == 0:
				commande = 'echo "' + titre + '" >> sav.nk'
				system_nk.execute(commande)
	else:											# Bonne page
		print "\033[1m\033[92mTopic added\033[0m"
		val = liste[0]
		liste.remove(val)
		if int(test) == 0:
			commande = 'echo "' + titre + '" >> sav.nk'
			system_nk.execute(commande)

def articles(titre, date, url, frame, chaine, liste, test):
	if test == 0:
		print "\033[1m\033[92mAdding topic on vogsphere\033[0m"
	admin(titre, date, url, frame, chaine, liste, test)
