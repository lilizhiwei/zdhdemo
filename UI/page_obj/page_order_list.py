from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from .page_all import page_all
import unittest

class order_list(page_all):

	#click
	def click_query(self):
		self.driver.find_element_by_xpath("//*[@class='js-search btn btn-success']").click()

	def click_insert(self):
		self.driver.find_element_by_xpath("//*[@class='js-add btn sbold btn-primary']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.visibility_of_element_located((By.XPATH,"//*[@class='js-source form-control js-filter-input']")))
		sleep(0.3)

	def click_preservation(self):
		self.driver.find_element_by_xpath("//*[@class='js-save btn btn-success pull-right']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.visibility_of_element_located((By.XPATH,"//*[@class='alert alert-message alert-dismissible fade in alert-success']/span")))

	def click_delete(self):
		self.driver.find_element_by_xpath("//*[@class='far fa-trash-alt']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.visibility_of_element_located((By.XPATH,"//*[text()='确认']")))

	def click_confirm(self):
		self.driver.find_element_by_xpath("//*[text()='确认']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.visibility_of_element_located((By.XPATH,"//*[@class='alert alert-message alert-dismissible fade in alert-success']/span")))


	#send_keys
	def send_id(self,name):
		self.driver.find_element_by_xpath("//*[@class='search-id form-control']").send_keys(name)

	def send_qdmc(self,name):
		self.driver.find_element_by_xpath("//*[@class='search-source form-control']").send_keys(name)

	def send_insert_qdmc(self,name):
		self.driver.find_element_by_xpath("//*[@class='js-source form-control js-filter-input']").send_keys(name)

	def send_day(self,name):
		self.driver.find_element_by_xpath("//*[@class='js-attributionCycle form-control js-filter-input']").send_keys(name)

	def send_click_id(self,name):
		self.driver.find_element_by_xpath("//*[@class='js-clickidPara form-control']").send_keys(name)
