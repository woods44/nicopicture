__author__ = 'g1244785'
#! /usr/bin/python
#-*- coding:utf-8-*-

class Data:
	def reading_ranking(self,a_opener):
		a_url = "http://seiga.nicovideo.jp/illust/ranking/point/hourly/g_creation"
		a_request = (a_url)
		a_html = a_opener.open(a_request).read()
		html = open('./output','wb')
		#print a_html
		html.write(a_html)
		html.close()