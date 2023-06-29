import hashlib

import redis

r = redis.Redis(host='localhost', port=6379, db='url_n3.new_table')

def get_short_url(url):
    short_url = r.get(url)
    if short_url:
        return short_url.decode('utf-8')

    url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()
    short_url = url_hash[:6]

    r.set(url, short_url)

    return short_url