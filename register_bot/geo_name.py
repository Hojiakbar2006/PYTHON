from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


def get_location_name(latitude, longitude):
	geolocator = Nominatim(user_agent="my_app")

	try:
		location = geolocator.reverse(f"{latitude}, {longitude}")
		return location.address

	except GeocoderTimedOut as e:
		print("Error: geocode failed on input %s with message %s" % (e.message))
