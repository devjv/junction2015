app.controller('MyOffersCtrl', ['$scope', '$rootScope','ParamsService',

    function($scope, $rootScope, ParamsService) {
        self = this;
        self.ordered_flights = [];

        $rootScope.currentPage = 'me';

        ParamsService.getUsersOffers().then(
            function(respose) {
                self.ordered_flights = respose.data.result.map(function(flight) {
                    flight.offered_flight.departure_time = new Date(flight.offered_flight.departure_time);
                    return flight;
                });
                console.log(self.ordered_flights);

            }
        );
    }
]);
