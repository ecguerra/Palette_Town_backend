from flask import Flask, g

import models
from resources.colors import colors
from resources.palettes import palettes
from resources.users import users

DEBUG=True
PORT=8000

app = Flask(__name__)

app.config.from_pyfile('config.py')

@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response    

app.register_blueprint(colors, url_prefix='/api/colors')
app.register_blueprint(palettes, url_prefix='/api/palettes')
app.register_blueprint(users, url_prefix='/api/users')

@app.route('/')
def index():
    return 'Homepage'

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)

