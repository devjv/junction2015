app.directive('flightBox', function() {
	return {
		templateUrl: 'static/flight-box.html',
		scope: {
			flight: '=',
			buttonAction: '='
		}
	};
});
