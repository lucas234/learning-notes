# @Time    : 2021/4/8 15:39
# @Author  : lucas
# @File    : connect_sql.py
# @Project : pyqt
# @Software: PyCharm

# # Microsoft sql
# import pymssql
# conn = pymssql.connect(server=server, user=user, password=password, database=db)
# cursor = conn.cursor()
# cursor.execute("SELECT COUNT(MemberID) as count FROM Members WHERE id = 1")
# row = cursor.fetchone()
# conn.close()
# print(row)
#
# # Postgres
#
# import psycopg2
# conn = psycopg2.connect(database=db, user=user, password=password, host=host, port="5432")
# cursor = conn.cursor()
# cursor.execute('SELECT COUNT(MemberID) as count FROM Members WHERE id = 1')
# row = cursor.fetchone()
# conn.close()
# print(row)
#
# # mysql
# import pymysql
# import mysql.connector
# import MySQLdb
# conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
# cursor = conn.cursor()
# cursor.execute('SELECT COUNT(MemberID) as count FROM Members WHERE id = 1')
# row = cursor.fetchone()
# conn.close()
# print(row)

# sqlite
# import sqlite3
# path = ""
# connection = sqlite3.connect(path)
# cursor = connection.cursor()
# cursor.execute("query")
# result = cursor.fetchall()
# connection.commit()

# # MongoDB
# import pymongo
#
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]


# pandas read pyodbc
# import pyodbc
# import pandas as pd
# #Create/Open a Connection to Microsoft's SQL Server
# conn = pyodbc.connect(CONNECTION_STRING)
# sql = "SELECT EmployeeID,EmployeeName FROM dbo.Employees"
# df = pd.read_sql(sql,conn)
# print(df.head())
# #Close the Connection
# conn.close()

import pyodbc
import sqlite3


SQL = "select * FROM tblUser where EmailAddress like 'lucas.liu@lexisnexis.com%'"
SQL1 = "select * FROM tblUser where EmailAddress = 'lucas.liu@lexisnexis.com'"
SQLITE = "test.db"

create_table = """
    create table settings(
        id int,
        concurrency int,
        downloadPath varchar,
        PRIMARY KEY(id)
    );
"""
insert = "insert into settings values(3, 93, 'c:\\')"
query = "select * from settings"

config = {"host": "",
          "db": "",
          "user": "",
          "pwd": "",
          }


class DBConnectors(object):
    def __init__(self):
        # sql_server = 'DRIVER={{SQL Server}};SERVER={host};DATABASE={db};UID={user};PWD={pwd}'.format(**config)
        # self.conn = pyodbc.connect(sql_server)
        # self.conn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
        # self.conn.setencoding(encoding='utf-8')

        # sqlite3
        self.conn = sqlite3.connect(SQLITE)
        self.cursor = self.conn.cursor()

    def query(self, sql):
        self.cursor.execute(sql)
        # row = self.cursor.fetchone()
        # results = []
        # while row:
        #     results.append(row)
        #     row = self.cursor.fetchone()
        # return results
        return [result for result in self.cursor]

    def execute(self, sql):
        """insert,update,delete some data"""
        try:
            count = self.cursor.execute(sql).rowcount
            self.conn.commit()
            print('Rows inserted/updated/deleted: ' + str(count))
        except:
            self.conn.rollback()

    def exec_procedure(self, store_procedure):
        """not use for sqlite3"""
        # uspGetAllUsers('999999')
        self.cursor.execute(f"{{CALL {store_procedure}}}")
        # self.conn.commit()
        return [result for result in self.cursor]

    def get_drivers(self):
        # 查看系统支持的driver
        print(pyodbc.drivers())
        return pyodbc.drivers()

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    print(123)
    # s = DBConnectors()

# print(s.query(query))
# s.execute(insert)
# print(s.exec_procedure("uspGetAllUsers('999999')"))
