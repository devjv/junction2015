app.controller('AddOffersCtrl', function($scope, $rootScope, $uibModalInstance) {
    $rootScope.currentPage = 'add';
    $scope.cancel = function() {
		$uibModalInstance.close();
    };
});
