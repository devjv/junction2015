app.controller('MyOffersCtrl', ['$scope', '$rootScope', '$uibModal', 'ParamsService',

    function($scope, $rootScope, $uibModal, ParamsService) {
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

        $scope.openDialog = function() {
            console.log($uibModal);
            $uibModal.open({
                templateUrl: 'static/add-offers.html',
                controller: 'AddOffersCtrl'
            });
        };
    }
]);
