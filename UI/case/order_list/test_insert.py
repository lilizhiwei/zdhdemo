from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,sys,os
sys.path.append("../../page_obj")
from page_obj.page_order_list import order_list
from page_obj.page_all import page_all

class insert(unittest.TestCase):
	'''渠道归因配置-新增'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_insert(self):
		#登录
		page_all(self.driver).login()
		#验证登录成功
		self.assertEqual(self.driver.find_element_by_xpath("//*[@class='navbar nav_title']/a/span").text,'数据管理平台')

		#进入渠道归因配置界面
		page_all(self.driver).click_jcpt()
		page_all(self.driver).click_jcgy()
		page_all(self.driver).click_ddgy()
		page_all(self.driver).click_qdgypz()

		#新增渠道归因配置并保存
		order_list(self.driver).click_insert()
		order_list(self.driver).send_insert_qdmc('UI_test')
		order_list(self.driver).send_day(7)
		order_list(self.driver).send_click_id('UI_test')
		order_list(self.driver).click_preservation()

		#验证新增成功
		self.assertEqual(self.driver.find_element_by_xpath("//*[@class='alert alert-message alert-dismissible fade in alert-success']/span").text,'成功')
		self.assertEqual(self.driver.find_element_by_xpath("//*[@class='td-source']").text,'UI_test')
		
		#删除数据
		order_list(self.driver).click_delete()
		order_list(self.driver).click_confirm()

		#验证删除成功
		self.assertEqual(self.driver.find_element_by_xpath("//*[@class='alert alert-message alert-dismissible fade in alert-success']/span").text,'成功')

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()