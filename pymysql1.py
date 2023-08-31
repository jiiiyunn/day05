import pymysql
from pymysql import cursors

connectionString = {
    'host': '192.168.111.10',
    'port' : 3306,
    'database': "study",
    'user' : 'student',
    'password' : '1234',
    'charset' : 'utf8'
}

try:  
    con = pymysql.connect(**connectionString)
    cursor = con.cursor(cursors.DictCursor)
    sql = "SELECT * FROM book"
    cursor.execute(sql)
    rows = cursor.fetchone()
    print(rows)
    con.close()
except Exception as e:
    print("예외발생 : ", e) 