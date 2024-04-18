import requests
import os
from dotenv import load_dotenv, find_dotenv
import geopy.distance
import requests



def search_map_by_name(firstArg):
    print("Retrieving...")
    search = str(firstArg.replace(" ", "+"))

    bulkText=""

    tooFar = False

    #load env variables
    load_dotenv(find_dotenv())

    # Configure your OpenAI API key
    map_api_key = os.environ.get("MAP_API_KEY")
    longLat = str(str(os.environ.get("LONGITUDE"))+","+str(os.environ.get("LATITUDE")))
    
    url=f'https://api.mapbox.com/search/searchbox/v1/suggest?q={search}&language=en&limit=10&navigation_profile=driving&eta_type=navigation&origin={longLat}&session_token=0a8f7baa-16d8-4ef1-88b1-c54bce4022c4&access_token={map_api_key}'
    response =requests.get(url)

    if response.status_code == 200:
        data = response.json()
        results = data['suggestions']

        if(len(results)==10):
            for x in range(1,len(results)):
                try:
                    restaurantName    = str(results[x]['name']+" - ")
                    restaurantAddress = str(results[x]['address']+" - ")
                    restaurantDistanceMeters= (results[x]['distance'])
                    restaurantDistance = str(round(restaurantDistanceMeters/1609))+" miles"
                    restaurantInfo = restaurantName+restaurantAddress+str(restaurantDistance)
                    #if any restaurant is 200 or more miles away
                    if (restaurantDistanceMeters>=321800):
                        tooFar=True
                        break
                    bulkText += restaurantInfo + "\n"
                except:
                    pass
        if(tooFar):
            return search_map_by_category(search)
        else:
            return (bulkText)
    else:
        return ("Request failed")
    
def search_map_by_category(firstArg):
    category = str(firstArg.replace("+", "_"))

    bulkText=""

    #load env variables
    load_dotenv(find_dotenv())

    # Configure your OpenAI API key
    map_api_key = os.environ.get("MAP_API_KEY")
    longLat = str(str(os.environ.get("LONGITUDE"))+","+str(os.environ.get("LATITUDE")))
    
    url=f'https://api.mapbox.com/search/searchbox/v1/category/{category}?&language=en&limit=10&navigation_profile=driving&origin={longLat}&access_token={map_api_key}'
    response =requests.get(url)

    if response.status_code == 200:
        data = response.json()
        results = data['features']

        if (len(results)<=1):
            return (f'No category matching {category}')
        
        for x in (range(len(results)-1)):
            restaurantName    = str(results[x]['properties']['name']+" - ")
            restaurantAddress = str(results[x]['properties']['address']+" - ")
            restaurantCoords = (float(results[x]['properties']['coordinates']['latitude']), float(results[x]['properties']['coordinates']['longitude']))
            localCoords = (os.environ.get("LATITUDE"), os.environ.get("LONGITUDE"))

            restaurantDistance = geopy.distance.geodesic(localCoords,restaurantCoords).miles
            restaurantInfo = restaurantName+restaurantAddress+(str(round(restaurantDistance, 2))+" miles")
            bulkText += restaurantInfo + "\n"



        return (bulkText)
    else:
        return ("Request failed")
if __name__ == '__main__':
    print(search_map_by_name("family"))