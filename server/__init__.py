from flask import Flask
from peewee import SqliteDatabase

db = SqliteDatabase("server/database/informations.db")
db.connect()

from server.models.information import Information
db.create_tables([Information])

app = Flask(__name__)
from server.routes import routes