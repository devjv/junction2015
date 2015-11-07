app.controller('UserOrdersController', function($scope) {
    $scope.message = "VITUN ORDERS";

    this.orders = [
        {'date': '2015-11-07', 'time': '11-00-00', 'year': '2015', 'airport': 'London', 'destination': 'Oakland'},
    ];
    /*

	Show all user orders

    One order:
    - departure date
    - departure time
    - departure year
	- departure air port
	- destination

    */


});