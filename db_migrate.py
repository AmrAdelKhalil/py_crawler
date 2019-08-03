from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)

POSTGRES = {
    'user': 'docker',
    'pw': 'docker',
    'db': 'youtube',
    'host': 'postgresql',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DATABASE URI configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
print(app.config['SQLALCHEMY_DATABASE_URI'])

# All migrations imports comes after this line
from models.videos import *

# Migration helpers to get things done
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
	manager.run()
