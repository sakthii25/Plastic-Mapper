from PIL import Image
import concurrent.futures
from geopy.geocoders import Nominatim

def get_city_from_coordinates(latitude, longitude):
    def _get_city_from_coordinates():
        try:
            geolocator = Nominatim(user_agent="myGeocoder")
            location = geolocator.reverse((latitude, longitude), exactly_one=True)

            if location is not None:
                address = location.raw.get("address", {})
                city = address.get("city") or address.get("town")
                return city
            else:
                return 'other'
        except:
            return 'other'

    try:
        # Create a ThreadPoolExecutor with a timeout of 1 second
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(_get_city_from_coordinates)
            city = future.result(timeout=2)
            return city

    except concurrent.futures.TimeoutError:
        return 'other'


def get_location(img_path):
    """
    Extract the geolocation information from the image using its EXIF data.

    Args:
        img_path (str): Path to the image file.

    Returns:
        list: [latitude, longitude] if geolocation data is available, [0, 0] otherwise.
    """
    try:
        # Open the image file
        img = Image.open(img_path)

        # Extract the EXIF data
        exif_data = img._getexif()

        # Check if EXIF data exists and if GPSInfo tag exists
        if exif_data and 0x8825 in exif_data:
            gps_info = exif_data[0x8825]

            # Extract latitude and longitude
            try:
                latitude = gps_info[2][0] + gps_info[2][1] / 60.0 + gps_info[2][2] / 3600.0
                longitude = gps_info[4][0] + gps_info[4][1] / 60.0 + gps_info[4][2] / 3600.0
            except:
                return [0,0]

            # Determine latitude reference (N/S)
            latitude_ref = gps_info[1]

            if latitude_ref == 'S':
                latitude = -latitude

            # Determine longitude reference (E/W)
            longitude_ref = gps_info[3]

            if longitude_ref == 'W':
                longitude = -longitude

            return [latitude, longitude]
        else:
            # Return [0, 0] if geolocation data is not found in the image
            return [0, 0]
    except:
        # Handle any other exceptions that may occur during the process
        return [0, 0]