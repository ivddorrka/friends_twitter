"""
Main module
"""
import json
import folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderUnavailable


def read_file(file):
    """
    Reads file, returns possible variants of further move
    """
    with open(file) as json_file:
        data = json.load(json_file)
    return data
# print(read_file('barackobama.json'))

def find_all_locs(file):
    """
    To get from json file a list o lists\
    with friends' names and their locations
    """
    data = read_file(file)
    needeed = data['users']
    names_locs = []
    for i in needeed:
        result = i['name'], i['location']
        names_locs.append(result)
    return names_locs
# print(find_all_locs('barackobama.json'))

def geopisition_users(file):
    """
    To find coordinates according to location
    """
    lst = find_all_locs(file)
    geolocator = Nominatim(user_agent="Friends geo")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=0.5)
    result = []
    for loc in lst:
        try:
            location = geolocator.geocode(loc[1])
            try:
                res = location.latitude, location.longitude
                result.append([loc[0], res])
            except AttributeError:
                continue
        except GeocoderUnavailable:
            continue
    return result
# print(geopisition_users('barackobama.json'))

def on_map(file):
    """
    To return a map to user
    """
    try:
        lst = geopisition_users(file)
        map = folium.Map(location=[33, -39], tiles="Stamen Terrain", zoom_start=3)
        for i in lst:
            folium.Marker([i[1][0], i[1][1]], popup="{}".format(i[0]), icon=folium.Icon(color='pink')).add_to(map)
        return map
    except KeyError:
        map = folium.Map(location=[33, -39], tiles="Stamen Terrain", zoom_start=3)
        return map
# print(on_map('barackobama.json'))