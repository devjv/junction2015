from sqlalchemy.orm import backref
from db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)


class Airport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(
        db.Unicode(255),
        nullable=False,
        unique=True
    )
    name = db.Column(
        db.Unicode(255),
        nullable=True
    )


class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination_airport_id = db.Column(
        db.Integer,
        db.ForeignKey(Airport.id, ondelete='RESTRICT'),
        nullable=False
    )
    destination_airport = db.relationship(
        'Airport',
        primaryjoin='Airport.id == Flight.destination_airport_id',
        backref=backref(
            'incoming_flights',
            cascade='all, delete-orphan',
            passive_deletes=True,
        )
    )
    departure_airport_id = db.Column(
        db.Integer,
        db.ForeignKey(Airport.id, ondelete='RESTRICT'),
        nullable=False
    )
    departure_airport = db.relationship(
        'Airport',
        primaryjoin='Airport.id == Flight.departure_airport_id',
        backref=backref(
            'departuring_flights',
            cascade='all, delete-orphan',
            passive_deletes=True,
        )
    )
    departure_time = db.Column(db.Date)
    arrival_time = db.Column(db.Date)
    code = db.Column(db.String(255))


class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(
        db.Integer,
        db.ForeignKey(User.id, ondelete='RESTRICT'),
        nullable=False
    )
    flight = db.Column(
        db.Integer,
        db.ForeignKey(Flight.id, ondelete='RESTRICT'),
        nullable=False
    )




class TradeRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    money = db.Column(db.Float, default=0)
    requesting_offer = db.Column(db.Integer,
        db.ForeignKey(Offer.id, ondelete='RESTRICT'),
        nullable=False
    )
    responding_offer = db.Column(db.Integer,
        db.ForeignKey(Offer.id, ondelete='RESTRICT'),
        nullable=False
    )
    fulfilled = db.Column(db.Boolean, default=false)



