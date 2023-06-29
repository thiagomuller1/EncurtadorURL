import pymysql as pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='moninha',
    db='url_n3'
)

conn = pymysql.connect('url_n3.db')

c = conn.cursor()
c.execute('''CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, long_url TEXT, short_url TEXT)''')
