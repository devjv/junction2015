app.controller('MyOffersCtrl', function($scope, $rootScope, $uibModal) {
    this.myoffers = [
        {'destination': 'Amsterdam', 'date': '2015-11-9', 'departure': '15:00', 'code': 'AY-8090 '},
        {'destination': 'Sydney', 'date': '2015-11-23', 'departure': '14:00', 'code': 'AY-8090 '},
        {'destination': 'London', 'date': '2015-12-29', 'departure': '18:00', 'code': 'AY-8090 '},
    ];
    // this.myoffers = [];
    $rootScope.currentPage = 'me';

    $scope.openDialog = function() {
        var modalInstance = $uibModal.open({
            templateUrl: 'static/add-offers.html',
            controller: 'AddOffersCtrl'
        });
    };
});
