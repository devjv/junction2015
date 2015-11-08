angular.module('myApp').factory('DataService', ['$q', '$http', 
	function ($http) {

		return ({
			getFlightsForUser: getFlightsForUser,
			getOffersForFlight: getOffersForFlight,
			getSimilarFlights: getSimilarFlights,
			getUsersOffers: getUsersOffers
		});


		function getFlightsForUser() {
			$http({
				url: '/flights',
				method: "GET"
			});
		}


		function getOffersForFlight(flight) {
			$http({
				url: '/offers_for_flight',
				method: "GET",
				data: {
					flight_id: flight.id
				}
			});
		}

		

		function getUsersOffers() {
			$http({
				url: '/users_offers',
				method: "GET"
			});
		}

		function getSimilarFlights(flight) {
			$http({
				url: '/near_flights',
				method: "GET",
				data: {
					flight_id: flight.id
				}
			});
		}


		function createNewOffer(flight) {
			$http({
				url: '/createnewoffer',
				method: "POST",
				data: {
					departure: flight.departure,
					arrival: flight.arrival
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
			});
		}



	}]);