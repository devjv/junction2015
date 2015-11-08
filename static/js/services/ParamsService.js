angular.module('myApp').factory('ParamsService', ['$http', 
	function ($http) {

		return ({
			getFlightsForUser: getFlightsForUser,
			getOffersForFlight: getOffersForFlight,
			getSimilarFlights: getSimilarFlights,
			getUsersOffers: getUsersOffers,
			createNewOffer: createNewOffer
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


		function createNewOffer(offeredFlight, nearFlights, prices) {
			return $http({
				url: '/createnewoffer',
				method: "POST",
				params: {
					flight_id: offeredFlight.id,
					near_flights: nearFlights,
					prices: prices
				}
			});
		}

		function acceptOffer(offer) {
			var matchingFlight;
			for (int i = 0; i < user.flights.size()) {
				if (user.flights[i].id == offer)
			}
			return $http({
				url: /acceptoffer',
				method: "POST",
				params: {

				}
			});
		}



	}]);