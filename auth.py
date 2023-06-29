from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_api_key(username, password):
    # Verifique se a chave API fornecida é válida
    return username == 'api_key' and password == 'api_secret'

if __name__ == '__main__':
    app.run(debug=True)
