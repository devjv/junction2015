import os
from flask import Flask
from assets import assets
from db import db
from app.views import api, others, user
from flask.ext.assets import Environment, Bundle


class Application(Flask):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(__name__)
        self.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        self.config['DEBUG'] = True

        # self.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        self.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
        db.init_app(self)
        self.register_blueprint(api)
        self.register_blueprint(user)
        self.register_blueprint(others)

        assets = Environment(self)
        assets.load_path = [
            os.path.join(os.path.dirname(__file__), 'bower_components'),
            os.path.join(os.path.dirname(__file__), 'static/js'),
            # os.path.join(os.path.dirname(__file__), 'bower_components'),
        ]
        assets.register(
            'js_all',
            Bundle(
                '**/**.min.js',
                'js/**.min.js',
                output='js_all.js'
            )
        )
