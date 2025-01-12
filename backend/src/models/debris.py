# backend/src/models/debris.py
from datetime import datetime
from app import db

class SpaceDebris(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    norad_id = db.Column(db.String(20), unique=True)
    position_x = db.Column(db.Float)
    position_y = db.Column(db.Float)
    position_z = db.Column(db.Float)
    velocity_x = db.Column(db.Float)
    velocity_y = db.Column(db.Float)
    velocity_z = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)