import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
sys.path.append("../db_fixture")
sys.path.append("../page_obj")
from db_fixture.test_data import sql
from page_obj.page_all import page_all

class deleteAudience(unittest.TestCase):
    #删除接口
    def setUp(self):
        self.base_url = page_all.url_100020905 + 'deleteAudience'

    def tearDown(self):
        pass

    def test_1(self):
        #productId存在 成功删除
        payload = {"productId":"1302","buType":"String","mediaValue":{"account_id":"8978752","dsp_id":"1","client_id":"2"}}
        r = requests.post(self.base_url, json=payload)
        self.result = r.json()
        print(self.result)
        self.assertEqual(self.result['status'], '0')

    def test_2(self):
        #productId不存在 删除错误
        payload = {"productId":"13011","buType":"String","mediaValue":{"account_id":"8978752","dsp_id":"1","client_id":"2"}}
        r = requests.post(self.base_url, json=payload)
        self.result = r.json()
        print(self.result)
        self.assertEqual(self.result['status'], '1')

if __name__ == '__main__':
    unittest.main()
