#!/usr/bin/python2.7

import string_nk

def str_replace(string):
    ret = str(string)
    retu = ret.replace("&#39;", "'")
    ret = retu.replace("&quot;", '"')
    retu = ret.replace("&amp;", '&')
    return retu

def str_replace2(string):
    ret = str(string)
    retu = ret.replace("&#39;", "'")
    ret = retu.replace("&quot;", '"')
    retu = ret.replace("&amp;", ' et ')
    ret = retu.replace('"', "'")
    retu = ret.replace("#", ' ')
    ret = retu.replace('!', " ")
    retu = ret.replace("?", ' ')
    ret = retu.replace('.', " ")
    retu = ret.replace(",", ' ')
    ret = retu.replace(';', "'")
    retu = ret.replace("[", '(')
    ret = retu.replace("]", ')')
    retu = ret.replace("{", '(')
    ret = retu.replace("}", ')')
    retu = ret.replace("/", ' ')
    ret = retu.replace("\\", ' ')
    return ret

def decoupe(string, start, size):
	index = 0
	ret = ""
	for lettre in string:
		if index >= start and size > 0:
			ret += lettre
			size-=1
		if size < 1:
			return ret
		index+=1
	return ret

def cut(string, delimiter, index):
	string.split
	for item in string.split(delimiter):
		if index == 0:
			return item
		index-=1
	return ""

def match(string, match):
	if match in string:
		return 1
	return 0
