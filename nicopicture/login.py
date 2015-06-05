__author__ = 'g1244785'
#! /usr/bin/env python
#-*- coding:utf-8 -*-

import urllib2
import cookielib
import urllib


class Login():
	def __init__(self):
		self._base_url = ('https://secure.nicovideo.jp/secure/login?site=niconico')
		self._username = ('hutakikanata805782@gmail.com')
		self._pass = ('hutakikanata1013')
	def login(self):
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		req = urllib2.Request(self._base_url)
		account = {"mail":self._username, "password":self._pass}
		req.add_data(req)
		return opener