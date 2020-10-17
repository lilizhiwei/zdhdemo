import requests
import unittest,sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
sys.path.append("../db_fixture")
sys.path.append("../page_obj")
from db_fixture.test_data import sql
from page_obj.page_all import page_all

class queryAudience(unittest.TestCase):
    #查询接口
    def setUp(self):
        self.base_url = page_all.url_100020905 + 'queryAudience'

    def tearDown(self):
        pass

    def test_1(self):
        #productId正确 成功查询
        payload = {'productId':'1301462','buType':'String','mediaValue':{'account_id':'8978752','dsp_id':'1','client_id':'2'}}
        r = requests.post(self.base_url, json=payload)
        self.result = r.json()
        print(self.result)
        self.assertEqual(self.result['status'], '0')
        self.assertEqual(self.result['mediaValue'], {'audience_id': '6242176', 'audience_status': 'PROCESSING'})

    def test_2(self):
        #productId不存在 查询不到
        payload = {'productId':'1301462111','buType':'String','mediaValue':{'account_id':'8978752','dsp_id':'1','client_id':'2'}}
        r = requests.post(self.base_url, json=payload)
        self.result = r.json()
        print(self.result)
        self.assertEqual(self.result['status'], '1')

if __name__ == '__main__':
    unittest.main()
