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

class query(unittest.TestCase):
	'''渠道归因配置-查询'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_query(self):
		#登录
		page_all(self.driver).login()
		#验证登录成功
		self.assertEqual(self.driver.find_element_by_xpath("//*[@class='navbar nav_title']/a/span").text,'数据管理平台')

		#进入渠道归因配置界面
		page_all(self.driver).click_jcpt()
		page_all(self.driver).click_jcgy()
		page_all(self.driver).click_ddgy()
		page_all(self.driver).click_qdgypz()

		#输入查询并查询
		order_list(self.driver).send_id(21)
		order_list(self.driver).send_qdmc('baidu_ocpc')
		order_list(self.driver).click_query()
		#验证查询结果
		WebDriverWait(self.driver,30,0.5).until(EC.visibility_of_element_located((By.XPATH,"//*[@class='td-source']")))
		self.assertEqual(self.driver.find_element_by_xpath("//*[@class='td-source']").text,'baidu_ocpc')

		
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()