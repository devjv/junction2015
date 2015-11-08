app.controller('FindOffersCtrl', ['$scope', '$rootScope', 'ParamsService',
    function($scope, $rootScope, ParamsService) {
    $scope.flight;

    $scope.flightChanged = function() {
        console.log($scope.flight);
    };


    $rootScope.currentPage = 'find';
    console.log($scope.flight);
    /*ParamsService.getOffersForFlight($scope.flight).then(
        function(respose) {
            console.log(respose);
            self.offers = respose.data.result.map(function(flight) {
                flight.offered_flight.departure_time = new Date(flight.offered_flight.departure_time);
                return flight;
            });
            console.log(self.ordered_flights);

        }
    );*/

}]);