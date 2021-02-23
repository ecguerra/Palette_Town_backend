from flask import Flask, g
from flask_cors import CORS, logging
from flask_login import LoginManager

import os

import models
from resources.colors import colors
from resources.palettes import palettes
from resources.app_users import app_users
from resources.color_palettes import color_palettes
from resources.saved_palettes import saved_palettes

DEBUG=True
PORT=8000

app = Flask(__name__)

app.config['SECRET_KEY']=(os.environ.get('SECRET_KEY'))

CORS(app, \
     origins=['http://localhost:3000','https://palettetown.netlify.app'], \
     supports_credentials=True)

logging.getLogger('flask_cors').level = logging.DEBUG

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'

@login_manager.user_loader
def load_user(user_id):
    try:
        return models.AppUser.get_by_id(user_id)
    except models.DoesNotExist:
        return None

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
app.register_blueprint(app_users, url_prefix='/api/app_users')
app.register_blueprint(color_palettes, url_prefix='/api/color_palettes')
app.register_blueprint(saved_palettes, url_prefix='/api/saved_palettes')

@app.route('/')
def index():
    return 'Homepage'

if 'ON_HEROKU' in os.environ:
    print('HEROKU SITE')
    models.initialize()

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)

