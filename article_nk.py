#!/usr/bin/python2.7

import control_nk

def admin(titre, date, url, frame, chaine):
	control_nk.dcp(196, 110, 1, 1)									# VGS #
	control_nk.dcp(226, 304, 1, 5)									# ADMIN #
	if control_nk.test_url("Administration - Panneau d'administration") == 0:
		articles(titre, date, url, frame, chaine)
	else:
		add_article(titre, date, url, frame, chaine)

def add_article(titre, date, url, frame, chaine):
	control_nk.dcp(1126, 285, 1, 5)									# nouvel article #
	if control_nk.test_url("Administration") == 0:
		articles(titre, date, url, frame, chaine)
	else:
		add_titre(titre, date, url, frame, chaine)

def add_titre(titre, date, url, frame, chaine):
	control_nk.dcp(173, 333, 1, 0)									# titre #
	title = "[" + chaine + "] " + titre
	control_nk.copier(title)
	control_nk.ctrl_V()
	categorie(titre, date, url, frame, chaine)

def categorie(titre, date, cat, frame, chaine):
	control_nk.dcp(577, 342, 1, 1)									# Categorie #
	control_nk.copier(cat)
	control_nk.ctrl_V()
	control_nk.dcp(463, 396, 1, 0)									# Video #
	frame2(titre, date, cat, frame, chaine)

def frame2(titre, date, url, frame, chaine):
	control_nk.dcp(77, 663, 1, 5)									# inserer le code #
	control_nk.copier(frame)
	control_nk.dcp(175, 357, 1, 1)									# HTML #
	control_nk.ctrl_V()
	control_nk.dcp(173, 249, 1, 3)									# inserer #
	param(titre, date, url, frame, chaine)

def param(titre, date, url, frame, chaine):
	control_nk.dcp(252, 285, 1, 1)									# parametre article #
	control_nk.dcp(217, 516, 1, 0)									# date de creation #
	date0 = date +  " 00:00:00"
	control_nk.copier(date0)
	control_nk.ctrl_V()
	control_nk.dcp(850, 332, 1, 1)									# date de pub #
	control_nk.copier(date0)
	control_nk.ctrl_V()
	enregistrer(titre, date, url ,frame, chaine)

def enregistrer(titre, date, url, frame, chaine):
	control_nk.dcp(149, 232, 1, 5)									# enregistrer #
	if control_nk.test_url("Administration") == 0:
		articles(titre, date, url, frame, chaine)

def articles(titre, date, url, frame, chaine):
	print "Ajout de l'article ..."
	admin(titre, date, url, frame, chaine)
	print "Article ajoute"
