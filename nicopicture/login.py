#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib2
import urllib
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
		return a_browser
