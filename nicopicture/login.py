#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib2
import urllib
import cookielib
from mechanize import Browser

"""
Login class

This class use login for niconico

Attribute:
base_url:login url
user_name:login user name for niconico
password:login password for niconico

return mechanize Browser

"""

class Login(object):
	def __init__(self):
		self._base_url = "https://account.nicovideo.jp/login?site=seiga"
		self._user_name = "hutakikanata805782@gmail.com"
		self._password = "hutakikanata1013"

	def login(self):
		a_browser = Browser()
		a_browser.open(self._base_url)
		a_browser.select_form(nr = 0)
		a_browser["mail_tel"] = self._user_name
		a_browser["password"] = self._password
		contents = a_browser.submit()
		#header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0' ,'Referer':'http://lohas.nicoseiga.jp/o/ff21b6920d3482f4f0d406bf875e8657e488cfd4/1434074767/4437929'}
		#request = urllib2.Request('http://lohas.nicoseiga.jp/priv/ff21b6920d3482f4f0d406bf875e8657e488cfd4/1434074767/4437929',None,header)
		#response =  br.open(request)
		#f = open("out","wb")
		#f.write(response.read())
		#f.close()
		#response.close()
		return a_browser
