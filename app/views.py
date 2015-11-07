# -*- encoding: utf-8 -*-
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


@api.route('/offers_for_users')
def offers_for_flight():
    flight_id = request.args.get('flight_id', None, type=int)
    if not flight_id:
        return jsonify({'error': 'Flight not found'})
    query = Offer.query.filter(
        Offer.requested_flight ==
        Flight.query.filter(Flight.id == flight_id)
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




# @api.route('/airports')
# def airports():
#     search = request.args.get('search', '')
#     if not search:
#         return jsonify({'error': 'search parameter required'})
#     query = Airport.query.filter(
#         db.or_(
#             Airport.name.ilike('%{}%'.format(search)),
#             # Airport.code.ilike('%{}%'.format(search))
#         )
#     )
#     return jsonify({
#         'result': [{
#             'name': airport.name,
#             'code': airport.code
#         } for airport in query.limit(10)]}
#     )
#
#     return str(query.count())
#
#
# @api.route('/flights')
# def flights():
#     departure = request.args.get('departure', '')
#     if not departure:
#         return jsonify({'error': 'departure required'})
#     destination = request.args.get('destination', '')
#     if not destination:
#         return jsonify({'error': 'destination required'})
#     departure_airport = Airport.query.filter(
#         Airport.code == departure
#     ).first()
#     if not departure_airport:
#         return jsonify({'error': 'departure airport not found'})
#     destination_airport = Airport.query.filter(
#         Airport.code == destination
#     ).first()
#     if not destination_airport:
#         return jsonify({'error': 'destination airport not found'})
#
#     query = Flight.query.filter(
#         Flight.destination_airport == destination_airport,
#         Flight.departure_airport == departure_airport
#     )
#     return jsonify({
#         'result': [{
#             'departure_time': str(flight.departure_time),
#             'code': flight.code
#         } for flight in query.limit(10)]}
#     )
#
#     return 'SUCCESS'
