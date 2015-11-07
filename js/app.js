var app = angular.module('myApp', ['ngRoute']);

app.config(function($routeProvider) {
    $routeProvider
    .when('/', {
        templateUrl : 'templates/login.html',
        controller  : 'LoginController'
    })
    .when('/login', {
        templateUrl : 'templates/login.html',
        controller  : 'LoginController'
    })
    .when('/flights', {
        templateUrl : 'templates/flights.html',
        controller  : 'AllOrdersController'
    })
    .when('/orders', {
        templateUrl : 'templates/orders.html',
        controller  : 'UserOrdersController'
    })
    .when('/createorder', {
        templateUrl : 'templates/createorder.html',
        controller  : 'CreateOrderController'
    })

;})