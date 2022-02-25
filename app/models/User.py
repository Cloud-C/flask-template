from sqlalchemy import func

from .models import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(300), nullable=False)
    status = db.Column(db.Integer, nullable=False, server_default='1')
    deleted_at = db.Column(db.DateTime)
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now())
