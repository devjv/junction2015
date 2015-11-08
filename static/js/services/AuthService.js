angular.module('myApp').factory('AuthService',
	['$q', '$timeout', '$http', function($q, $timeout, $http) {


		var user;
		var userStatus = null;

		return ({
			login: login,
			logout: logout,
			register: register
		});

		function login(username, password) {
			var deferred = $q.defer();

			$http.post('/login', {
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

			$http.get('/logout')
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




	}]);



