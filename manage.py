from flask import current_app
import os
from flask.ext.script import Manager, Server

port = 5000
if 'PORT' in os.environ:
    port = os.environ['PORT']

def create_app():
    from application import Application
    return Application()


manager = Manager(create_app)
manager.add_command("runserver", Server(port=port))


@manager.shell
def make_shell_context():
    from db import db
    context = {}
    context['app'] = current_app
    context['db'] = db
    context.update(db.Model._decl_class_registry)
    return context


@manager.command
def dropdb():
    from db import db
    db.drop_all()


@manager.command
def createdb():
    from db import db
    db.create_all()


if __name__ == "__main__":
    manager.run()
