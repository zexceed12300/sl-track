function getLocation() {
  if (navigator.geolocation) {
    var options = {timeout:30000, enableHighAccuracy: true, maximumage: 0};
    navigator.geolocation.getCurrentPosition(showPosition, showError, options);
  }
}
getLocation();

function showPosition(position) {
  var lat = position.coords.latitude;
  var long = position.coords.longitude;
  var acc = position.coords.accuracy;

  $.ajax({
    type: 'POST',
    url: 'modules/geolocation/ajax.php',
    data: {Lat: lat, Long: long, Acc: acc},
    mimType: 'text'
  });
}

function showError(error) {
	switch(error.code) {
		case error.PERMISSION_DENIED:
			var denied = 'User denied the request for Geolocation';
            break;
		case error.POSITION_UNAVAILABLE:
			var unavailable = 'Location information is unavailable';
			break;
		case error.TIMEOUT:
			var timeout = 'The request to get user location timed out';
			break;
		case error.UNKNOWN_ERROR:
			var unknown = 'An unknown error occurred';
			break;
  }
}