#!/usr/bin/python2.7

import spider_nk
import string_nk
import system_nk
import control_nk
import os, sys

def	start():
	pid = os.getpid()
	commande = 'echo "' + str(pid) + '" > spider.pid'
	system_nk.execute(commande)
	print "\t\tSpider\t  - Crawler -\t v 1.0\n"
	print "\033[93m\033[1m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m\033[94m"
	print "\033[97mProcess ID \t\t[\033[93m\033[1m" + str(pid)  + "\033[0m\033[97m]"
	control_nk.init_ctrl()

if __name__=='__main__':
	start()
	mark = system_nk.contenue("mark.nk")
	mark = string_nk.decoupe(mark, 0, len(mark) - 1)
	if len(sys.argv) == 3:
		spider_nk.spider(sys.argv[1], sys.argv[2])
	if len(sys.argv) == 2:
		spider_nk.spider(sys.argv[1], -1)
	else:
		spider_nk.spider(mark, -1)
		com = "echo '0' > mark.nk"
		system_nk.execute(com)
