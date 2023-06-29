import hashlib
from importlib.resources import Resource

import pymysql
import hashlib

import pymysql


def shorten_url(url):
    conn = pymysql.connect('url_n3.new_table.db')
    c = conn.cursor()

    url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()
    short_url = url_hash[:6]

    c.execute("INSERT INTO urls (long_url, short_url) VALUES (?, ?)", (url, short_url))
    conn.commit()

    return short_url

class ShortenerAPI(Resource):
    def get(self, short_id):
        cursor = db.cursor()
        sql = "SELECT url FROM urls WHERE short_url=%s"
        val = (f'short.ly/{short_id}', )
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            return {'url': result[0]}
        else:
            return {'error': 'URL not found'}, 404
