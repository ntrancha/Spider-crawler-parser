#!/usr/bin/python2.7

import string_nk

def mois_recup(string):
	strin = string_nk.cut(string, " ", 2)
	if string_nk.match(strin, "Jan"):
		return "1"
	if string_nk.match(strin, "Feb"):
		return "2"
	if string_nk.match(strin, "Mar"):
		return "3"
	if string_nk.match(strin, "Apr"):
		return "4"
	if string_nk.match(strin, "May"):
		return "5"
	if string_nk.match(strin, "Jun"):
		return "6"
	if string_nk.match(strin, "Jul"):
		return "7"
	if string_nk.match(strin, "Aug"):
		return "8"
	if string_nk.match(strin, "Sep"):
		return "9"
	if string_nk.match(strin, "Oct"):
		return "10"
	if string_nk.match(strin, "Nov"):
		return "11"
	if string_nk.match(strin, "Dec"):
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
			ret 
def jour_recup(string):
	format_date(string_nk.cut(string, " ", 1))
	return string_nk.cut(string, " ", 1)

def annee_recup(string):
	return string_nk.cut(string, " ", 3)

def seconde_recup(string):
	return string_nk.cut(string_nk.cut(string, " ", 4), ":", 2)

def minute_recup(string):
	return string_nk.cut(string_nk.cut(string, " ", 4), ":", 1)

def heure_recup(string):
	return string_nk.cut(string_nk.cut(string, " ", 4), ":", 0)

