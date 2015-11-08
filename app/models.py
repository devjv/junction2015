from sqlalchemy.orm import backref
from db import db


users_flight = db.Table(
    'users_flight',
    db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('flight_id', db.Integer, db.ForeignKey('flight.id'))
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    flights = db.relationship('Flight', secondary=users_flight)


class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    destination = db.Column(
        db.Unicode(255),
        nullable=False
    )
    departure = db.Column(
        db.Unicode(255),
        nullable=False
    )
    departure_time = db.Column(db.Date)
    # arrival_time = db.Column(db.Date)
    code = db.Column(db.String(255))
    users = db.relationship('User', secondary=users_flight)

# association_table = Table('association', Base.metadata,
#     Column('left_id', Integer, ForeignKey('left.id')),
#     Column('right_id', Integer, ForeignKey('right.id'))
# )
#
# class Parent(Base):
#     __tablename__ = 'left'
#     id = Column(Integer, primary_key=True)
#     children = relationship("Child",
#                     secondary=association_table)


class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    offered_flight_id = db.Column(
        db.Integer,
        db.ForeignKey(Flight.id, ondelete='RESTRICT'),
        nullable=False
    )
    offered_flight = db.relationship(
        'Flight',
        primaryjoin='Flight.id == Offer.offered_flight_id',
        backref=backref(
            'offers_1',
            cascade='all, delete-orphan',
            passive_deletes=True,
        )
    )
    requested_flight_id = db.Column(
        db.Integer,
        db.ForeignKey(Flight.id, ondelete='RESTRICT'),
        nullable=False
    )
    requested_flight = db.relationship(
        'Flight',
        primaryjoin='Flight.id == Offer.requested_flight_id',
        backref=backref(
            'offers_2',
            cascade='all, delete-orphan',
            passive_deletes=True,
        )
    )

    creator_id = db.Column(
        db.Integer,
        db.ForeignKey(User.id, ondelete='RESTRICT'),
        nullable=False
    )
    creator = db.relationship(
        'User',
        primaryjoin='User.id == Offer.creator_id',
        backref=backref(
            'offers_created',
            cascade='all, delete-orphan',
            passive_deletes=True,
        )
    )

    accepter_id = db.Column(
        db.Integer,
        db.ForeignKey(User.id, ondelete='RESTRICT'),
        nullable=False
    )
    accepter = db.relationship(
        'User',
        primaryjoin='User.id == Offer.accepter_id',
        backref=backref(
            'offers_accepted',
            cascade='all, delete-orphan',
            passive_deletes=True,
        )
    )
