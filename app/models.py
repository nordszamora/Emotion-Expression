from datetime import datetime, timezone
from . import db

class Emotion(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   raw_text = db.Column(db.String(255), nullable=True)
   processed_text = db.Column(db.String(255), nullable=True)
   date = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
   label = db.Column(db.Integer, nullable=True)
