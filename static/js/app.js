var app = angular.module('myApp', ['ngRoute', 'ngAnimate', 'ui.bootstrap']);

app.config(function($routeProvider, $locationProvider) {
  $routeProvider
  .when('/', {
    templateUrl: 'static/home.html',
    controller: function($rootScope) {
      $rootScope.currentPage = undefined;
    }
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
  .when('/find', {
    templateUrl: 'static/find-offers.html',
    controller: 'FindOffersCtrl'
  })
  .otherwise({
    templateUrl: 'static/404.html'
  });

  $locationProvider.html5Mode(true);
});
