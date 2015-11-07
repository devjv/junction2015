import dateutil.parser
from flask import json
import sqlalchemy
from app import Airport, Flight
from application import Application
from db import db

app = Application()


def import_airports():
    data = json.loads(open('import_data/airports_data.json').read())
    for line in data:
        try:
            airport = Airport(
                name=line[u'name'],
                code=line[u'iata']
            )
            db.session.add(airport)
            db.session.commit()
            print 'imported', line[u'iata']
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            print 'couldnt importj', line[u'iata']
            # u'status': 1,
            # u'name': u'Yining Airport',
            # u'iata': u'YIN',
            # u'lon': u'81.33144',
            # u'iso': u'CN',
            # u'lat': u'43.952',
            # u'type': u'airport',
            # u'continent': u'AS',
            # u'size': u'small'


def import_routes():
    data = json.loads(open('import_data/flight_data.json').read())
    for line in data:
        try:
            print line['destination'], line['departure']
            destination = Airport.query.filter_by(code=line['destination']).one()
            departure = Airport.query.filter_by(code=line['departure']).one()

            flight = Flight(
                destination_airport=destination,
                departure_airport=departure,
                departure_time=dateutil.parser.parse(line['time']),
                code=line['flight']
            )

            db.session.add(flight)
            db.session.commit()

            # print 'imported destination, departure, line
            print 'EI VIRHE'
        except sqlalchemy.orm.exc.NoResultFound:
            print 'VIRHE'
            # airport = Airport(
            #     name=line[u'name'],
            #     code=line[u'iata']
            # )
            # db.session.add(airport)

            # u'destination': u'LEQ',
            # u'flight': u'5Y* 8',
            # u'departure': u'ISC',
            # u'time': u'2015-11-06T06:54:00.000Z'


with app.app_context():
    import_airports()
    import_routes()
