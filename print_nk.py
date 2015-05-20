#!/usr/bin/python2.7

def printr(string, color, gras, tab):
	space = " "
	espace = ""
	if color == "Black":
		color = "30"
	elif color == "Blue":
		color = "34"
	elif color == "Green":
		color = "32"
	elif color == "Cyan":
		color = "36"
	elif color == "Red":
		color = "31"
	elif color == "Purple":
		color = "35"
	elif color == "Orange":
		color = "33"
	else:
		color = "37"
	while tab > 0:
		tab -= 1
		espace += space
	if gras != 1:
		gras = 0
	return espace + "\033[" + str(gras) + "m\033[" + str(color) + "m" + string + "\033[0m"

def printc(string, color, gras, tab):
	space = " "
	espace = ""
	if color == "Black":
		color = "30"
	elif color == "Blue":
		color = "34"
	elif color == "Green":
		color = "32"
	elif color == "Cyan":
		color = "36"
	elif color == "Red":
		color = "31"
	elif color == "Purple":
		color = "35"
	elif color == "Orange":
		color = "33"
	else:
		color = "37"
	while tab > 0:
		tab -= 1
		espace += space
	if gras != 1:
		gras = 0
	print espace + "\033[" + str(gras) + "m\033[" + str(color) + "m" + string + "\033[0m"
