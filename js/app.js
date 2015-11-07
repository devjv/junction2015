var app = angular.module('myApp', ['ngRoute']);

app.config(function($routeProvider) {
	$routeProvider
    .when('/', {
    	templateUrl : 'templates/login.html',
    	controller  : 'LoginController'
    })

    .when('/orders', {
    	templateUrl : 'templates/login.html',
    	controller  : 'OrdersController'
    });
})