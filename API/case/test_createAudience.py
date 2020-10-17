import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
sys.path.append("../db_fixture")
sys.path.append("../page_obj")
from db_fixture.test_data import sql
from page_obj.page_all import page_all

class createAudience(unittest.TestCase):
    #新增接口
    def setUp(self):
        self.base_url = page_all.url_100020905 + 'createAudience'

    def tearDown(self):
        pass

    def test_1(self):
        #参数正确，成功创建
        payload = {"productId":"1314","buType":"String","mediaValue":{"account_id":"8978752","dsp_id":"1","client_id":"2","type":"CUSTOMER_FILE","name":"测试101"}}
        r = requests.post(self.base_url, json=payload)
        self.result = r.json()
        print(self.result)
        self.assertEqual(self.result['status'], '0')
        self.assertEqual(self.result['mediaValue'], {"audience_id":"6348288"})

    def test_2(self):
        #参数正确且name重复 创建失败
        payload = {"productId":"13140","buType":"String","mediaValue":{"account_id":"8978752","dsp_id":"1","client_id":"2","type":"CUSTOMER_FILE","name":"测试100"}}
        r = requests.post(self.base_url, json=payload)
        self.result = r.json()
        print(self.result)
        self.assertEqual(self.result['status'], '1')

if __name__ == '__main__':
    unittest.main()
