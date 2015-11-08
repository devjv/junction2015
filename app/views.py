# -*- encoding: utf-8 -*-
import datetime
from flask import Blueprint, request, jsonify, make_response, render_template
from app import Flight, User, Offer
from db import db

api = Blueprint('api', __name__, url_prefix='/api')
others = Blueprint('others', __name__)


@api.app_errorhandler(404)
def index(err):
    return render_template('index.html')


def format_flight(flight):
    return {
        'id': flight.id,
        'destination': flight.destination,
        'departure': flight.departure,
        'departure_time': str(flight.departure_time)
    }


@api.route('/flights')
def flights():
    query = Flight.query.filter(
        # Flight.
        # TODO: Suodatus käyttäjän mukaan
    )
    list = [
        format_flight(flight) for flight in query
    ]
    return jsonify({'result': list})


@api.route('/offers_for_flight')
def offers_for_flight():
    flight_id = request.args.get('flight_id', None, type=int)
    if not flight_id:
        return jsonify({'error': 'Flight not found'})
    query = Offer.query.filter(
        Offer.requested_flight_id == flight_id
        # TODO: Suodatus käyttäjän mukaan
    )
    list = [
        format_flight(offer.offered_flight) for offer in query
    ]
    return jsonify({'result': list})


@api.route('/users_offers')
def users_offers():
    query = Offer.query.filter(
        # TODO: Suodatus käyttäjän mukaan
    )
    list = [
        format_flight(offer.offered_flight) for offer in query
    ]
    return jsonify({'result': list})


@api.route('/near_flights')
def near_flight():
    flight_id = request.args.get('flight_id', None, type=int)
    flight = Flight.query.filter(
        Flight.id == flight_id
    ).one()
    query = Flight.query.filter(
        db.and_(
            Flight.departure_time < datetime.timedelta(days=1) + flight.departure_time,
            Flight.departure_time > datetime.timedelta(days=1) - flight.departure_time
        )
    )
    list = [
        format_flight(flight) for flight in query
    ]
    return jsonify({'result': list})
