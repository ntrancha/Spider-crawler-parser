#!/usr/bin/python2.7
	
import string_nk
import control_nk
import os, sys
import system_nk

def add(chaine, categorie, fichier, num):
	url = "https://www.youtube.com/"
	control_nk.dcp(765, 84, 1, 1)		# Barre url
	control_nk.ctrl("a")
	control_nk.copier(url)
	control_nk.ctrl_V()
	control_nk.enter()
	system_nk.paus("3")
	control_nk.dcp(258, 157, 1, 1)		# Barre recherche
	control_nk.ctrl("a")
	control_nk.copier(chaine)
	control_nk.ctrl_V()
	control_nk.enter()
	system_nk.paus("3")
	control_nk.dcp(467, 211, 1, 1)		# Filtres
	control_nk.dcp(529, 294, 1, 2)		# Chaines
	control_nk.dcp(529, 294, 1, 3)		# Premiere chaine
	control_nk.dcp(765, 84, 1, 1)		# Barre url
	control_nk.ctrl("a")
	control_nk.copier(url)
	control_nk.ctrl_C()
	adr = control_nk.xclip()
	adresse = adr + "/videos"
	test = 'grep "' + adresse + '" ' + fichier + " | wc -l > test.txt"
	system_nk.execute(test)
	ret = system_nk.contenue("test.txt")
	if string_nk.match(ret, "0") == 1:
		commande = 'echo "' + chaine + ';' + adresse + ';' + categorie + '" >> ' + fichier
		system_nk.execute(commande)
		print "================Nouveau flux youtube======================"
		print str(num) + " : " + chaine + " [" + categorie + "]"
		print adresse
	else:
		print "=======================Erreur============================="
		print "[deja present] (" + chaine + ")"

def multi(fichier_tmp, categorie, fichier):
	mon_fichier = open(fichier_tmp, "r")
	contenu = mon_fichier.readlines()
	mon_fichier.close()
	num = 0
	for line in contenu:
		ligne = string_nk.decoupe(line, 0, len(line) - 1)
		titre = string_nk.cut(ligne, ";", 0)
		categorie = string_nk.cut(ligne, ";", 1)
		num += 1
		add(titre, categorie, fichier, num)

if __name__=='__main__':
	control_nk.init_ctrl()
	if len(sys.argv) == 4:
		if string_nk.match(sys.argv[1], "txt") == 1:
			if string_nk.match(sys.argv[2], "fichier") == 1:
				print "File input  : " + sys.argv[1]
				print "File Ouput  : " + sys.argv[3]
				multi(sys.argv[1], sys.argv[2], sys.argv[3])
			else:
				print "Chaine    : " + sys.argv[1]
				print "Categorie : " + sys.argv[2]
				print "Fichier   : " + sys.argv[3]
				add(sys.argv[1], sys.argv[2], sys.argv[3], 1)
		else:
			print "Chaine    : " + sys.argv[1]
			print "Categorie : " + sys.argv[2]
			print "Fichier   : " + sys.argv[3]
			add(sys.argv[1], sys.argv[2], sys.argv[3], 1)
	else:
		print "Erreur"
		print "add_flux.py [Chaine] [Categorie] [Fichier de sortie]"
		print "add_flux.py [Fichier entree] fichier [Fichier de sortie]"
