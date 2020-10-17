from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import unittest

class page_all(object):
	#用户登录页面

	username = '***'
	password = '***'
	url = 'http:/***/index.html'

	def __init__(self, driver,user=username,pwd=password,url=url):
		self.user = user
		self.pwd = pwd
		self.url = url
		self.driver = driver

	#登录
	def login(self):
		self.driver.get(self.url)
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		self.driver.find_element_by_id("eid").send_keys(self.user)
		self.driver.find_element_by_id("pwd").send_keys(self.pwd)
		self.driver.find_element_by_id("btnSubmit").click()
		WebDriverWait(self.driver,30,0.5).until(EC.visibility_of_element_located((By.XPATH,"//*[@class='navbar nav_title']/a/span")))
		sleep(0.2)

	#click
	def click_jcpt(self):
		self.driver.find_element_by_link_text("监测平台").click()

	def click_jcgy(self):
		self.driver.find_element_by_link_text("监测归因").click()

	def click_ddgy(self):
		self.driver.find_element_by_link_text("订单归因").click()

	def click_qdgypz(self):
		self.driver.find_element_by_link_text("渠道归因配置").click()
		WebDriverWait(self.driver,30,0.5).until(EC.visibility_of_element_located((By.XPATH,"//*[@class='title_left']/h3")))