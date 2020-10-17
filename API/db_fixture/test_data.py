import sys
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

class sql(object):
    def select_demo(select_sql):
        r = DB().select(select_sql)
        return r
        
    def insert_demo(insert_sql):
        DB().insert(insert_sql)

    def delete_demo(delete_sql):
        DB().insert(delete_sql)


if __name__ == '__main__':
    unittest.main()
