# coding=utf8
import pymysql.cursors
import os
import configparser as cparser

#数据库配置-准备数据-需要单独测试数据库

# ======== Reading db_config.ini setting ===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/') # 获取绝对路径 反斜杠为兼容linux
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()

cf.read(file_path)
# 获取数据库配置信息
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db   = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


# 连接数据库 
class DB:

    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # 操作数据库
    def select(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            e = print("Error:数据库连接错误")

    def insert(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            e = print("Error:数据库连接错误")

    def delete(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            e = print("Error:数据库连接错误")

    # close database
    def close(self):
        self.connection.close()


if __name__ == '__main__':
    unittest.main()
    ''' 
    real_sql = "select sid from mktappmarketingdb.dmp_order_performance_param_config where id=1;"
    r = DB().select_demo(real_sql)
    print(r)
    real_sql1 = "INSERT INTO mktappmarketingdb.dmp_order_performance_param_config (`allianceid`, `sid`, `accountid`, `DataChange_CreateTime`, `DataChange_LastTime`, `ouid`) VALUES ('6', '77', '1', '2019-05-21 14:22:10', '2019-05-21 16:22:10', 'gdt_pairui_2513920509_test');"
    DB().insert_demo(real_sql1)
    real_sql2 = "DELETE FROM mktappmarketingdb.dmp_order_performance_param_config WHERE id=425;"
    DB().delete_demo(real_sql2)
    '''

