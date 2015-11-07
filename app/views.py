from flask import Blueprint, request, jsonify, make_response, render_template
from app import Airport, Flight
from db import db

api = Blueprint('api', __name__, url_prefix='/api')
others = Blueprint('others', __name__)


@others.route('/')
def index():
    return render_template('index.html')
    return make_response(open('templates/index.html').read())


@api.route('/airports')
def airports():
    search = request.args.get('search', '')
    if not search:
        return jsonify({'error': 'search parameter required'})
    query = Airport.query.filter(
        db.or_(
            Airport.name.ilike('%{}%'.format(search)),
            # Airport.code.ilike('%{}%'.format(search))
        )
    )
    return jsonify({
        'result': [{
            'name': airport.name,
            'code': airport.code
        } for airport in query.limit(10)]}
    )

    return str(query.count())


@api.route('/flights')
def flights():
    departure = request.args.get('departure', '')
    if not departure:
        return jsonify({'error': 'departure required'})
    destination = request.args.get('destination', '')
    if not destination:
        return jsonify({'error': 'destination required'})
    departure_airport = Airport.query.filter(
        Airport.code == departure
    ).first()
    if not departure_airport:
        return jsonify({'error': 'departure airport not found'})
    destination_airport = Airport.query.filter(
        Airport.code == destination
    ).first()
    if not destination_airport:
        return jsonify({'error': 'destination airport not found'})

    query = Flight.query.filter(
        Flight.destination_airport == destination_airport,
        Flight.departure_airport == departure_airport
    )
    return jsonify({
        'result': [{
            'departure_time': str(flight.departure_time),
            'code': flight.code
        } for flight in query.limit(10)]}
    )

    return 'SUCCESS'
