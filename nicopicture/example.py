__author__ = 'g1244785'
#! /usr/bin/env/ python
#-*- coding:utf-8 -*-

import sys
import urllib2
import login
import data

class Example(object):
	def main(self):
		print("aaaa")
		a_login = login.Login()
		a_opener = a_login.login()
		d = data.Data()
		d.reading_ranking(a_opener)
		return
