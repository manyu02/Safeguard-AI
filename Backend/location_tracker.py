# from opencage.geocoder import OpenCageGeocode

# api_key = "f6fa9d1614854ce4a4fc4f80ff171397"
# geocoder = OpenCageGeocode(api_key)

# location = "New Delhi"
# result = geocoder.geocode(location)

# if result:
#     lat, lng = result[0]['geometry']['lat'], result[0]['geometry']['lng']
#     print(f"Latitude: {lat}, Longitude: {lng}")
# else:
#     print("Location not found.")

from opencage.geocoder import OpenCageGeocode

# Replace with your OpenCage API Key
API_KEY = "f6fa9d1614854ce4a4fc4f80ff171397"
geocoder = OpenCageGeocode(API_KEY)

def get_coordinates(address):
    result = geocoder.geocode(address)
    
    if result:
        lat, lng = result[0]['geometry']['lat'], result[0]['geometry']['lng']
        return lat, lng
    else:
        return None

if __name__ == "__main__":
    address = input("Enter your address or city: ")
    coordinates = get_coordinates(address)
    
    if coordinates:
        print(f"Latitude: {coordinates[0]}, Longitude: {coordinates[1]}")
    else:
        print("Location not found.")
