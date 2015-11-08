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
				url: '/api/createnewoffer',
				method: "POST",
				params: {
					flight_id: offeredFlight.id,
					near_flights: nearFlights,
					prices: prices
				}
			});
		}

		function acceptOffer(offer) {
			return $http({
				url: '/acceptoffer',
				method: "POST",
				params: {
					offer_id: offer.id
				}
			});
		}



	}]);