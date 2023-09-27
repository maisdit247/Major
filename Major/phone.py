import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import subprocess


from geopy.geocoders import Nominatim


# pour retrouver la localisation
from opencage.geocoder import OpenCageGeocode


# geolocaliser lng, lat sur une map
# import folium

import os

# touver le pays du num
num = "+33666107204"
monNum = phonenumbers.parse(num)


# si ligne valide
# valid = phonenumbers.is_valid_number(monNum)
# print(valid)

# si possible
# possible = phonenumbers.is_possible_number(monNum)
# print(possible)

# trouver le pays
pays = geocoder.description_for_number(monNum, "fr")
print("Pays ", pays)

# timezone
timezon = timezone.time_zones_for_number(monNum)
print("Zone ", timezon)

# trouver operateur mobile
operateur = carrier.name_for_number(phonenumbers.parse(num), "fr")
print("Opérateur mobile ", operateur)

# GEOPY
app = Nominatim(user_agent="JournalDev")
location = app.geocode(timezon)  # .raw
# print(location.address)
print("Lat et lng de timezone ", location.latitude, location.longitude)
# print(location.raw)


# trouver longitude et latitude pour ceci pip install opencage
# s'inscrire au site ensuite dans geocoding API copier API keys
# key = "97c9fab42e154354a259125991b2246e"
# coord = OpenCageGeocode(key)
# requete = str(pays)
# reponse = coord.geocode(requete)
# print(reponse)
# extraire long et latt de reponse
# lat = reponse[0]["geometry"]["lat"]
# lng = reponse[0]["geometry"]["lng"]
# os.system("clear")
# print(num, pays, operateur, timezon)
# print(lat, lng)

# creation de la map
# maMap = folium.Map(location=[lat, lng], zoom_start=12)
# folium.Marker([lat, lng], popup=localisation).add_to(maMap)
# maMap.save("map.html")
