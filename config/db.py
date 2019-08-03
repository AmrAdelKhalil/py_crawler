from flask import Flask

app = Flask(__name__)

POSTGRES = {
    'user': 'crawler',
    'pw': '1234567',
    'db': 'py_crawler',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DATABASE URI configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES