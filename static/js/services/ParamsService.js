angular.module('myApp').factory('ParamsService', ['$http', 
	function ($http) {

		return ({
			getFlightsForUser: getFlightsForUser,
			getOffersForFlight: getOffersForFlight,
			getSimilarFlights: getSimilarFlights,
			getUsersOffers: getUsersOffers
		});


		function getFlightsForUser() {
			return $http({
				url: '/api/flights',
				method: "GET"
			});
		}


		function getOffersForFlight(flight) {
			return $http({
				url: '/api/offers_for_flight',
				method: "GET",
				params: {
					flight_id: flight.id
				}
			});
		}

		

		function getUsersOffers() {
			return $http({
				url: '/api/users_offers',
				method: "GET"
			});
		}

		function getSimilarFlights(flight) {
			return $http({
				url: '/api/near_flights',
				method: "GET",
				params: {
					flight_id: flight.id
				}
			});
		}


		// function createNewOffer(flight) {
		// 	return $http({
		// 		url: '/createnewoffer',
		// 		method: "POST",
		// 		params: {
		// 			departure: flight.departure,
		// 			arrival: flight.arrival
		// 			// Get back to this, unable to post a list of flights as query params
		// 		}
		// 	});
		// }

		// function acceptOffer(offer) {
		// 	var matchingFlight;
		// 	for (int i = 0; i < user.flights.size()) {
		// 		if (user.flights[i].id == offer)
		// 	}
		// 	return $http({
		// 		url: /acceptoffer',
		// 		method: "POST",
		// 		params: {

		// 		}
		// 	});
		// }



	}]);