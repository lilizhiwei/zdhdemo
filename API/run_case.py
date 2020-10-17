import time, sys
sys.path.append('./test_report')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data

if __name__ == "__main__":

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './test_report/' + now + '_result.html'

    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况')
    
    discover = unittest.defaultTestLoader.discover('./case',pattern='test_*.py')
    runner.run(discover)
    fp.close()