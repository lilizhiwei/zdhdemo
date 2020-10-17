import unittest
import requests
import os, sys

class page_all(object):
	#存放接口url前缀和cookie

	url_100020905 = 'http://***:8080/api/'

	def __init__(self, driver,url_100020905=url_100020905):
		self.url_100020905 = url_100020905
