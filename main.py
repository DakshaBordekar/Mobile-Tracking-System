import phonenumbers
from phonenumbers import geocoder
import folium

key="747be03ca74a4500a27d1ea46d07ee4a"

number=input("Enter the number with country code: ")
check_number=phonenumbers.parse(number)
number_location=geocoder.description_for_number(check_number,'en')
print("Country:",number_location)

from phonenumbers import carrier
service_provider=phonenumbers.parse(number)
print("Service Provider:",carrier.name_for_number(service_provider,'en'))

from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode(key)

query=str(number_location)
results=geocoder.geocode(query)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print("Latitude:",lat,"Longitude:",lng)

map_location=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=number_location).add_to(map_location)
map_location.save("mylocation.html")