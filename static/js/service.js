angular.module('myApp').factory('DataService', ['$q', '$http', 
	function ($http) {

		// var user = AuthService.getUser();
		var flight1 = {code: "asd123", departure: "Helsinki-Vantaa", arrival: "Heathrow", time: "17:00"}
		var user = {
			id: 12352376,
			flights: [			
				flight1,
				flight1
			],
			email: "testuser@testemail.test"
		}

		return ({
			getFlightsForPassenger: getFlightsForPassenger,
			getSimilarFlights: getSimilarFlights,
			getUsersOffers: getUsersOffers,
			getOffersForFlight: getOffersForFlight
		})


		function getFlightsForUser() {
			var user = user; //Placeholder
			$http({
				url: '/getflightsforuser',
				method: "GET",
				data: {
					user_id: user.id,
				}
			});
		}


		function getSimilarFlights(flight) {
			$http({
				url: '/getsimilarflights',
				method: "GET",
				data: {
					departure: flight.departure,
					arrival: flight.arrival,
					time: flight.time
				}
			});
		}

		function getUsersOffers() {
			$http({
				url: '/getflightsforuser',
				method: "GET",
				data: {
					user_id: user.id
				}
			});
		}

		function getOffersForFlight(flight) {
			$http({
				url: '/getflightsforuser',
				method: "GET",
				data: {
					departure: flight.departure,
					arrival: flight.arrival
				}
			});
		}

		function createNewOffer(flight) {
			$http({
				url: '/createnewoffer',
				method: "POST",
				data: {
					departure: flight.departure,
					arrival: flight.arrival,
					// Get back to this, unable to post a list of flights as query params
				}
			});
		}

		function acceptOffer(offer) {
			var matchingFlight;
			for (int i = 0; i < user.flights.size()) {
				if (user.flights[i].id == offer.)
			}
			$http({
				url: /acceptoffer',
				method: "POST",
				data: {

				}
			})
		}



	}]);