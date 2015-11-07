var app = angular.module('myApp', ['ngRoute']);

app.config(function($routeProvider) {
    $routeProvider
    .when('/', {
        templateUrl : 'static/login.html',
        controller  : 'LoginController'
    })
    .when('/login', {
        templateUrl : 'static/login.html',
        controller  : 'LoginController'
    })
    .when('/flights', {
        templateUrl : 'static/flights.html',
        controller  : 'AllOrdersController',
        controllerAs : 'allorders'
    })
    .when('/orders', {
        templateUrl : 'static/orders.html',
        controller  : 'UserOrdersController',
        controllerAs : 'orders'
    })
    .when('/createorder', {
        templateUrl : 'static/createorder.html',
        controller  : 'CreateOrderController'
    })

;})
