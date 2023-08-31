from pymysql import connect

connectionString = {
    'host': '192.168.111.10',
    'port' : 3306,
    'database': "study",
    'user' : 'studdent',
    'password' : '1234',
    'charset' : 'utf8'
}

try:  
    with connect(**connectionString) as con :
        cursor = con.cursor()
        sql = "INSERT INTO book_category VALUES(default, '끝',0)"
        cursor.execute(sql)
        con.commit()
except Exception as e:
    print(e) 