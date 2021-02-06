from peewee import *
from flask_login import UserMixin

import datetime
import config as cfg

DATABASE = PostgresqlDatabase(cfg.DB_DEV['name'],host=cfg.DB_DEV['host'],user=cfg.DB_DEV['user'],password=cfg.DB_DEV['password'],port=cfg.DB_DEV['port'])

class BaseModel(Model):
    class Meta:
        database = DATABASE

class Color(BaseModel):
    name = CharField()
    hex_name = CharField()
    rgb_name = CharField()
    hsl_name = CharField()
    cmyk_name = CharField()

class AppUser(UserMixin, BaseModel):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

class Palette(BaseModel):
    name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    app_user = ForeignKeyField(AppUser, backref='palettes')
    # might need another field for Likes?

class ColorPalette(BaseModel):
    color = ForeignKeyField(Color, backref='on_palettes')
    palette = ForeignKeyField(Palette, backref='used_colors')

class SavedPalette(BaseModel):
    app_user = ForeignKeyField(AppUser, backref='saved_by')
    palette = ForeignKeyField(Palette, backref='saved_palettes')

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Color, Palette, AppUser, ColorPalette, SavedPalette], safe=True)
    print('TABLES CREATED')
    DATABASE.close()