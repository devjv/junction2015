from flask import Flask
from db import db
from app.views import api


class Application(Flask):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(__name__)
        self.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        self.config['DEBUG'] = True

        # self.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        self.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
        db.init_app(self)
        self.register_blueprint(api)
