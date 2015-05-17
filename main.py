#!/usr/bin/python2.7

import spider_nk
import control_nk
import os, sys

if __name__=='__main__':
	control_nk.init_ctrl()
	if len(sys.argv) == 3:
		spider_nk.spider(sys.argv[1], sys.argv[2])
	if len(sys.argv) == 2:
		spider_nk.spider(sys.argv[1], -1)
	else:
		spider_nk.spider(0, -1)
