#! /usr/bin/env/ python
#-*- coding:utf-8 -*-
__author__ = 'g1244785'


import sys
import urllib2
import login
import data
import os
from mechanize import Browser

class Example(object):
	def main(self):

		args = sys.argv
		if len(args) == 3:
			user_name = str(args[1])
			pass_w = str(args[2])
		a_login = login.Login(user_name,pass_w)
		a_browser = a_login.login()
		d = data.Data(a_browser)
		path = os.path.join("..","picture")
		path_a = os.path.join("..","picture","adult")
		if not os.path.exists(path):
			print "Create:"+str(path)
			os.makedirs(path)
		if not os.path.exists(path_a):
			print "Create:"+str(path_a)
			os.makedirs(path_a)
		#d.adult_ranking()
		#d.fanart_ranking()
		d.legend_ranking()
		#d.reading_ranking()
		return
