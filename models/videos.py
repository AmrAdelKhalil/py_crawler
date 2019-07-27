from flask_sqlalchemy import SQLAlchemy
from __main__ import app

db = SQLAlchemy(app)
class Videos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_url = db.Column(db.String(128))
    title = db.Column(db.String(128))
    duration = db.Column(db.Integer)
    views = db.Column(db.Integer)
    thumbnail = db.Column(db.String(128))
    image = db.Column(db.String(128))
    