#!/usr/bin/python2.7

import control_nk
import system_nk

def test_url(string):
    system_nk.paus(1)
    com = system_nk.commande("wmctrl -l | grep Mozilla")
    if string_nk.match(com, string) == 0:
        return 0
    return 1

def admin(titre, date, url, frame):
    control_nk.dcp(196, 110, 1, 1)									# VGS #
    control_nk.dcp(226, 304, 1, 3)									# ADMIN #
    if test_url("Administration - Panneau d'administration") == 0:
        articles(titre, date, url, frame)
    else:
        add_article(titre, date, url, frame)

def add_article(titre, date, url, frame):
    control_nk.dcp(1126, 285, 1, 3)									# nouvel article #
    if test_url("Gestion des articles : Ajouter un article") == 0:
        articles(titre, date, url, frame)
    else:
        add_titre(titre, date, url, frame)

def add_titre(titre, date, url, frame):
    control_nk.dcp(173, 333, 1, 1)									# titre #
    control_nk.copier(titre)
    control_nk.ctrl("v")
    categorie(titre, date, url, frame)

def categorie(titre, date, url, frame):
    control_nk.ddcp(577, 342, 1, 1)									# Categorie #
    system_nk.execute('xdotool key V')
    control_nk.dcp(463, 396, 1, 1)									# Video #
    frame2(titre, date, url, frame)

def frame2(titre, date, url, frame):
    control_nk.dcp(77, 663, 1, 3)									# inserer le code #
    control_nk.copier(frame)
    control_nk.ddcp(175, 357, 1, 1)									# HTML #
    control_nk.ctrl("v")
    control_nk.dcp(173, 249, 1, 1)									# inserer #
    param(titre, date, url, frame)

def param(titre, date, url, frame):
    control_nk.dcp(252, 285, 1, 1)									# parametre article #
    control_nk.dcp(217, 516, 1, 1)									# date de creation #
    date0 = date +  " 00:00:00"
    control_nk.copier(date0)
    control_nk.ctrl("v")
    control_nk.dcp(850, 332, 1, 1)									# date de pub #
    control_nk.copier(date0)
    control_nk.ctrl("v")
    enregistrer(titre, date, url ,frame)

def enregistrer(titre, date, url, frame):
    control_nk.dcp(149, 232, 1, 3)									# enregistrer #

def articles(titre, date, url, frame):
    admin(titre, date, url, frame)
