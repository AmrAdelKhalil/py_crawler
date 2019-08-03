from flask import Flask

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