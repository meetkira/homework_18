from marshmallow import Schema, fields

from setup_db import db


class Director(db.Model):
    """Director database model"""
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class DirectorSchema(Schema):
    """Director Schema"""
    id = fields.Int()
    name = fields.Str()
