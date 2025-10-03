from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    credits_questions = db.Column(db.Integer, default=20)
    credits_reports = db.Column(db.Integer, default=10)

class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_type = db.Column(db.String)  # 'upload' or 'news'
    name = db.Column(db.String)
    url = db.Column(db.String, nullable=True)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

class Chunk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    chunk_text = db.Column(db.Text)
    position = db.Column(db.Integer)

class AskLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    question = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    used_credits_question = db.Column(db.Integer, default=0)
    used_credits_report = db.Column(db.Integer, default=0)