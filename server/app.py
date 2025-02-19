#!/usr/bin/env python3

from models import db, Scientist, Mission, Planet
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask import Flask, make_response, jsonify, request
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")


igrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def home():
    return ''


if __name__ == '__main__':
    app.run(port=5555, debug=True)
