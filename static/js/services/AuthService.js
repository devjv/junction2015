angular.module('myApp').factory('AuthService',
	['$q', '$timeout', '$http', function($q, $timeout, $http) {


		var user;
		var userStatus = null;

		return ({
			login: login,
			logout: logout,
			// register: register,
			isLoggedIn: isLoggedIn
		});

		function login(username, password) {
			var deferred = $q.defer();

			$http.post('/user/login', {
				username: username, password: password
			})
			.success(function(data, status) {
				if (status === 200 && data.status) {
					user = undefined;
					deferred.reject();
				} else {
					userStatus = false;
					deferred.reject();
				}
			})
			.error(function(data) {
				userStatus = false;
				deferred.reject();
			});

			return deferred.promise;
		}

		function logout() {
			var deferred = $q.defer();

			$http.get('/user/logout')
			.success(function(data) {
				userStatus = false;
				user = undefined;
				deferred.resolve();
			})
			.error(function(data) {
				userStatus = false;
				deferred.reject();
			});

			return deferred.promise;
		}


		// Registering is disabled, because we assume that the users are
		// registered and authenticated via external systems
		// by the airline companies
		function register(username, password) {
			var deferred = $q.defer();

			$http.post('/register', {
				username: username,
				password: password
			})
			.success(function(data, success) {
				if (status === 200 && data.status) {
					deferred.resolve();
				} else {
					deferred.reject();
				}
			})
			.error(function(data) {
				deferred.reject();
			});

			return deferred.promise;
		}

		function isLoggedIn() {
			return !!userStatus
		}




	}]);



