from urllib import request

from flask import Flask
from flask_restful import Api, Resource
import mysql.connector
import redis

app = Flask(__name__)
api = Api(app)

class ShortenerAPI(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

api.add_resource(ShortenerAPI, '/shorten')


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="url_n3"
)

redis_client = redis.Redis(host='localhost', port=6379)

def generate_short_url():
    counter = redis_client.incr('counter')
    return f'short.ly/{counter}'

def save_url(url, short_url):
    cursor = db.cursor()
    sql = "INSERT INTO urls (url, short_url) VALUES (%s, %s)"
    val = (url, short_url)
    cursor.execute(sql, val)
    db.commit()

class ShortenerAPI(Resource):
    def post(self):
        url = request.json['url']
        short_url = generate_short_url()
        save_url(url, short_url)
        return {'short_url': short_url}, 201

class ShortenerAPI(Resource):
    def get(self, short_id):
        cursor = db.cursor()
        sql = "SELECT url FROM urls WHERE short_url=%s"
        val = (f'short.ly/{short_id}',)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            return {'url': result[0]}
        else:
            return {'error': 'URL not found'}, 404

if __name__ == '__main__':
    app.run(debug=True)