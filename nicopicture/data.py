#! /usr/bin/python
#-*- coding:utf-8-*-
__author__ = 'g1244785'

import re
import os.path
import urllib2
import HtmlGetter
import time
from mechanize import Browser



class Data(object):
	def __init__(self, a_browser):
		self._a_browser = a_browser
		self._a_getter = HtmlGetter.HtmlGetter(self._a_browser)

	def reading_ranking(self):
		a_image_url_list = []
		a_url_pat = re.compile('<a class="center_img_inner " href="(.*)" >')
		a_url = 'http://seiga.nicovideo.jp/illust/ranking/point/hourly/g_creation'
		a_html = self._a_getter.html_get(a_url)
		a_image_url_list = a_url_pat.findall(a_html)
		print a_image_url_list
		for a_image_url in a_image_url_list:
			time.sleep(1)
			self.image_get(a_image_url)

	def image_get(self, a_url):
		a_image_url = ''
		a_image_pat = re.compile('<a href="(.*)" id="illust_link" target="_blank">')
		a_base_url = "http://seiga.nicovideo.jp"
		a_html = self._a_getter.html_get(a_url)
		a_image_url = a_image_pat.search(a_html)
		a_image_url = a_base_url + a_image_url.group(1)
		self.image_download(a_image_url, a_url)

	def image_download(self, a_image_url, a_url):
		a_title_pat = re.compile('<title>(.*) -')
		a_image_pat = re.compile('<img src="(.*)" data-watch_url')
		a_title = ''
		a_image = ''
		a_html = self._a_getter.html_get_refere(a_image_url, a_url)
		a_base_url = "http://lohas.nicoseiga.jp"
		a_title = a_title_pat.search(a_html)
		a_title = a_title.group(1)
		print a_title
		a_image = a_image_pat.search(a_html)
		a_image = a_base_url + a_image.group(1)
		print a_image
		a_image_file = self._a_getter.html_get_refere(a_image, a_image_url)
		f = open("./picture/"+str(a_title), "wb")
		f.write(a_image_file)
		f.close()



