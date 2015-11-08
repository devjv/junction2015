# -*- encoding: utf-8 -*-
import datetime
from flask import Flask, session, Blueprint, request, jsonify, make_response, render_template
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
        'departure_time': str(flight.departure_time),
        'code': flight.code
    }

@api.route('/login', methods=['POST'])
def login():
    json_data = request.json
    user = User.query.filter_by(email=json_data['email']).first()
    if user and bcrypt.check_password_hash(
            user.password, json_data['password']):
        session['logged_in'] = True
        status = True
    else:
        status = False
    return jsonify({'result': status})


@api.route('/logout')
def logout():
    session.pop('logged_in', None)
    return jsonify({'result': 'success'})





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
        {
            'offered_flight': format_flight(offer.offered_flight),
            'id': offer.id
        }
        for offer in query
    ]
    return jsonify({'result': list})


@api.route('/users_offers')
def users_offers():
    query = Offer.query.filter(
        # TODO: Suodatus käyttäjän mukaan
    )
    list = [
        {
            'offered_flight': format_flight(offer.offered_flight),
            'id': offer.id
        }
        for offer in query
    ]
    return jsonify({'result': list})


@api.route('/near_flights')
def near_flight():
    flight_id = request.args.get('flight_id', None, type=int)
    if not flight_id:
        return jsonify({'error': 'flight_id required'})
    flight = Flight.query.filter(
        Flight.id == flight_id
    ).first()
    if not flight:
        return jsonify({'error': 'Flight not found for id'})
    query = Flight.query.filter(
        db.and_(
            Flight.departure_time <
            datetime.timedelta(days=1) + flight.departure_time,
            Flight.departure_time >
            datetime.timedelta(days=1) - flight.departure_time
        )
    )
    list = [
        format_flight(flight) for flight in query
    ]
    return jsonify({'result': list})
