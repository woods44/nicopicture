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
		print "reading ranking..."
		a_image_url_list = []
		a_url_pat = re.compile('<a class="center_img_inner " href="(.*)" >')
		a_url = 'http://seiga.nicovideo.jp/illust/ranking/point/hourly/g_creation'
		a_html = self._a_getter.html_get(a_url)
		a_image_url_list = a_url_pat.findall(a_html)
		#print a_image_url_list
		for a_image_url in a_image_url_list:
			time.sleep(1)
			self.image_get(a_image_url)

	def fanart_ranking(self):
		print "fan art ranking"
		a_image_url_list = []
		a_url_pat = re.compile('<a class="center_img_inner " href="(.*)" >')
		a_url = 'http://seiga.nicovideo.jp/illust/ranking/point/hourly/g_fanart'
		a_html = self._a_getter.html_get(a_url)
		a_image_url_list = a_url_pat.findall(a_html)
		#print a_image_url_list
		for a_image_url in a_image_url_list:
			time.sleep(1)
			self.image_get(a_image_url)

	def  legend_ranking(self):
		print "legend ranking"
		a_image_url_list = []
		a_url_pat = re.compile('<a class="center_img_inner " href="(.*)" >')
		a_url = 'http://seiga.nicovideo.jp/illust/ranking/point/hourly/g_popular'
		a_html = self._a_getter.html_get(a_url)
		a_image_url_list = a_url_pat.findall(a_html)
		#print a_image_url_list
		for a_image_url in a_image_url_list:
			time.sleep(1)
			self.image_get(a_image_url)

	def adult_ranking(self):
		print "adult reading"
		a_image_url_list = []
		a_url_pat = re.compile('<a class="center_img_inner " href="(.*)" >')
		a_url = 'http://seiga.nicovideo.jp/illust/ranking/point/hourly/g_adult'
		user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:9.0.1) Gecko/20100101 Firefox/9.0.1"
		request = urllib2.Request(a_url)
		response = self._a_browser.open(request)
		self._a_browser.select_form(nr = 1)
		response = self._a_browser.submit()
		response = self._a_browser.open(request)
		a_html = response.read()
		a_image_url_list = a_url_pat.findall(a_html)
		#print a_image_url_list
		for a_image_url in a_image_url_list:
			time.sleep(1)
			self.adult_image_get(a_image_url)

	def adult_image_get(self,a_url):
		a_image_url = ''
		a_image_pat = re.compile('<a href="(.*)" target="_blank" style="display:block;" id="illust_link">')
		a_title_pat = re.compile('<title>(.*) - ニコニコ春画</title>')
		a_base_url = "http://seiga.nicovideo.jp"
		a_html = self._a_getter.html_get(a_url)
		a_title = a_title_pat.search(a_html)
		a_title = a_title.group(1)
		a_title = re.sub("/", "_", a_title)
		a_image_url = a_image_pat.search(a_html)
		print a_title
		a_image_url = a_base_url + a_image_url.group(1)
		self.adult_image_download(a_image_url, a_url, a_title)

	def image_get(self, a_url):
		a_image_url = ''
		a_image_pat = re.compile('<a href="(.*)" id="illust_link" target="_blank">')
		a_base_url = "http://seiga.nicovideo.jp"
		a_html = self._a_getter.html_get(a_url)
		a_image_url = a_image_pat.search(a_html)
		a_image_url = a_base_url + a_image_url.group(1)
		self.image_download(a_image_url, a_url)

	def adult_image_download(self, a_image_url, a_url, a_title):
		a_image = ''
		a_html = self._a_getter.html_get_refere(a_image_url, a_url)
		f = open("../picture/adult/"+str(a_title)+".jpg", "wb")
		f.write(a_html)
		f.close()

	def image_download(self, a_image_url, a_url):
		a_title_pat = re.compile('<title>(.*) -')
		a_image_pat = re.compile('<img src="(.*)" data-watch_url')
		a_title = ''
		a_image = ''
		a_html = self._a_getter.html_get_refere(a_image_url, a_url)
		a_base_url = "http://lohas.nicoseiga.jp"
		a_title = a_title_pat.search(a_html)
		a_title = a_title.group(1)
		a_title = re.sub("/", "_", a_title)
		print a_title
		a_image = a_image_pat.search(a_html)
		a_image = a_base_url + a_image.group(1)
		print a_image
		a_image_file = self._a_getter.html_get_refere(a_image, a_image_url)
		f = open("../picture/"+str(a_title)+".jpg", "wb")
		f.write(a_image_file)
		f.close()



