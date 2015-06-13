#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'g1244785'


import urllib2
from mechanize import Browser

class HtmlGetter(object):
	def __init__(self, a_browser):
		self._a_browser = a_browser

	def html_get(self, a_url):
		request = urllib2.Request(a_url)
		try:
			response = self._a_browser.open(request)
		except urllib2.HTTPError, e:
			print ("Cannot this page be opened. reason to"+e)
		a_html = response.read()
		return a_html

	def html_get_refere(self, a_url, a_referer):
		user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:9.0.1) Gecko/20100101 Firefox/9.0.1"
		a_header = {'User-Agent':user_agent, 'Referer':a_referer}
		try:
			request = urllib2.Request(a_url, None, a_header)
			response = self._a_browser.open(request)
		except urrllib2.HTTPError, e:
			print ("Cannot this page be opened. reason to"+e)
		a_html = response.read()
		return a_html
