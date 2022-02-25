from importlib import import_module

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app
from app.models.models import db

app = create_app()

db.init_app(app)

import_module('app.models')

migrate = Migrate(app, db, compare_type=True)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
