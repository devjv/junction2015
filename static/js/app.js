var app = angular.module('myApp', ['ngRoute', 'ngAnimate']);

app.config(function($routeProvider, $locationProvider) {
  $routeProvider
  .when('/', {
    templateUrl: 'static/home.html'
  })
  .when('/login', {
    templateUrl: 'static/login.html',
    controller: 'LoginCtrl'
  })
  .when('/me', {
    templateUrl: 'static/my-offers.html',
    controller: 'MyOffersCtrl',
    controllerAs: 'myoffers'
  })
  .when('/add', {
    templateUrl: 'static/add-offers.html',
    controller: 'AddOffersCtrl'
  })
  .when('/find', {
    templateUrl: 'static/find-offers.html',
    controller: 'FindOffersCtrl'
  })
  .otherwise({
    template: 'page not found'
  });

  $locationProvider.html5Mode(true);
});
