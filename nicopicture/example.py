#! /usr/bin/env/ python
#-*- coding:utf-8 -*-
__author__ = 'g1244785'


import sys
import urllib2
import login
import data
from mechanize import Browser

class Example(object):
	def main(self):
		a_login = login.Login()
		a_browser = a_login.login()
		d = data.Data(a_browser)
		d.reading_ranking()
		return
