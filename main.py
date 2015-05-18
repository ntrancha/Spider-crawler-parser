#!/usr/bin/python2.7

import spider_nk
import system_nk
import control_nk
import os, sys

def	start():
	pid = os.getpid()
	commande = 'echo "' + str(pid) + '" > spider.pid'
	system_nk.execute(commande)
	print "Spider   - Crawler -\nv 1.0\n\nProcess ID : " + str(pid) + "\n"
	control_nk.init_ctrl()

if __name__=='__main__':
	start()
	if len(sys.argv) == 3:
		spider_nk.spider(sys.argv[1], sys.argv[2])
	if len(sys.argv) == 2:
		spider_nk.spider(sys.argv[1], -1)
	else:
		spider_nk.spider(0, -1)
