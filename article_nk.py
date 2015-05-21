#!/usr/bin/python2.7

import control_nk
import print_nk
import spider_nk
import string_nk
import crawler_nk
import system_nk

def admin(titre, date, url, frame, chaine, liste, test):
	print_nk.printc("Connection to vogsphere", "Blue", 0, 0)
	control_nk.dcp(196, 110, 1, 2)									# VGS #
	control_nk.dcp(226, 304, 1, 6)									# ADMIN #
	if control_nk.test_url("Administration - Panneau d'administration") == 0:
		articles(titre, date, url, frame, chaine, liste, test)
	else:
		print_nk.printc("Connected", "Green", 1, 2)
		add_article(titre, date, url, frame, chaine, liste, test)

def add_article(titre, date, url, frame, chaine, liste, test):
	print_nk.printc("New topic", "Blue", 0, 0)
	control_nk.dcp(1126, 285, 1, 6)									# nouvel article #
	if control_nk.test_url("Administration") == 0:
		articles(titre, date, url, frame, chaine, liste, test)
	else:
		add_titre(titre, date, url, frame, chaine, liste, test)

def add_titre(titre, date, url, frame, chaine, liste, test):
	print_nk.printc("Titre", "Orange", 0, 2)
	control_nk.dcp(173, 333, 1, 2)									# titre #
	title = "[" + chaine + "] " + titre
	control_nk.copier(title)
	control_nk.ctrl_V()
	print_nk.printc(titre, "White", 1, 4)
	categorie(titre, date, url, frame, chaine, liste, test)

def categorie(titre, date, cat, frame, chaine, liste, test):
	print_nk.printc("Category", "Orange", 0, 2)
	control_nk.dcp(577, 342, 1, 2)									# Categorie #
	control_nk.copier(cat)
	control_nk.ctrl_V()
	print_nk.printc(cat, "White", 1, 4)
	control_nk.dcp(463, 396, 1, 2)									# Video #
	frame2(titre, date, cat, frame, chaine, liste, test)

def frame2(titre, date, url, frame, chaine, liste, test):
	print_nk.printc("Insert video", "Orange", 0, 2)
	control_nk.dcp(77, 663, 1, 5)									# inserer le code #
	control_nk.copier(frame)
	control_nk.dcp(175, 357, 1, 2)									# HTML #
	control_nk.ctrl_V()
	print_nk.printc(frame, "White", 1, 4)
	control_nk.dcp(173, 249, 1, 5)									# inserer #
	param(titre, date, url, frame, chaine, liste, test)

def param(titre, date, url, frame, chaine, liste, test):
	print_nk.printc("Date", "Orange", 0, 2)
	control_nk.dcp(252, 285, 1, 5)									# parametre article #
	control_nk.dcp(217, 516, 1, 2)									# date de creation #
	date0 = date +  " 00:00:00"
	control_nk.copier(date0)
	control_nk.ctrl_V()
	print_nk.printc(date, "White", 1, 4)
	control_nk.dcp(850, 332, 1, 2)									# date de pub #
	control_nk.copier(date0)
	control_nk.ctrl_V()
	enregistrer(titre, date, url ,frame, chaine, liste, test)

def enregistrer(titre, date, url, frame, chaine, liste, test):
	print_nk.printc("Save", "Orange", 0, 2)
	control_nk.dcp(149, 232, 1, 9)									# enregistrer #
	testa = system_nk.commande('grep "'+titre+'" sav.nk | wc -l')
	modif = control_nk.test_url("Modifier")
	ajout = control_nk.test_url("Ajouter")
	num = test
	test += 1
	if modif == 1:
		print "\033[1m\033[92mTopic added\033[0m"
		val = liste[0]
		liste.remove(val)
		if int(testa) == 0:
			print "\033[93mAdd topic"
			commande = 'echo "' + string_nk.str_replace2(titre) + '" >> sav.nk'
	elif ajout == 1:		
		print "\033[1m\033[91mTopic exist\033[0m"
		val = liste[0]
		liste.remove(val)
		if int(testa) == 0:
			print "\033[93mAdd topic"
			commande = 'echo "' + string_nk.str_replace2(titre) + '" >> sav.nk'
	else:
		if test == 0:
			print "\033[1m\033[91mError topic. New try\033[0m"
			spider_nk.sav_article(liste, test)
		else:
			print "\033[1m\033[91mError topic\033[0m"
			val = liste[0]
			liste.remove(val)

def articles(titre, date, url, frame, chaine, liste, test):
	if test == 0:
		print_nk.printc("Adding topic on vogsphere", "Green", 0, 2)
	admin(titre, date, url, frame, chaine, liste, test)
