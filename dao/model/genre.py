from marshmallow import Schema, fields

from setup_db import db


class Genre(db.Model):
    """Genre database model"""
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class GenreSchema(Schema):
    """Genre Schema"""
    id = fields.Int()
    name = fields.Str()
