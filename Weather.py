import os
import requests
import json
import datetime
from dotenv import load_dotenv, find_dotenv


def current_weather(firstArg = ""):
    print("Getting weather...")

    #load env variables
    load_dotenv(find_dotenv())

    location = firstArg.rstrip('0123456789')
    if (location == ""):
        location = os.environ.get("CITY_STATE")

    # Configure your OpenAI API key
    weather_api_key = os.environ.get("WEATHER_API_KEY")
    
    url=f'http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={location}&aqi=no'
    response =requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return ("Request failed")
    
def weather_forecast(firstArg):
    print("Getting forecast...")

    #load env variables
    load_dotenv(find_dotenv())
    days = 3
    bulkText = ""
    location = firstArg.rstrip('0123456789')
    if (not location):
        location = os.environ.get("CITY_STATE")

    # Configure your OpenAI API key
    weather_api_key = os.environ.get("WEATHER_API_KEY")
    
    url=f'http://api.weatherapi.com/v1/forecast.json?key={weather_api_key}&q={location}&days={days}&aqi=no'
    response =requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for day in range(int(days)):
            dayInfo = data['forecast']['forecastday'][day]['date']
            bulkText+= str(dayInfo)     
            dayForecast = data['forecast']['forecastday'][day]['day']
            bulkText+= str(dayForecast)
        return(bulkText)

    else:
        return ("Request failed")

def moon_phase(firstArg = "current"):
    print("Getting moon phase...")
    
    #load env variables
    load_dotenv(find_dotenv())

    if (firstArg == "current"):
        date = datetime.datetime.now()
        location = os.environ.get("CITY_STATE")
    else:
        date = datetime.datetime.now()
        location = firstArg.rstrip('0123456789')


    # Configure your OpenAI API key
    weather_api_key = os.environ.get("WEATHER_API_KEY")
    
    url=f'http://api.weatherapi.com/v1/astronomy.json?key={weather_api_key}&q={location}&dt={date}'

    response =requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return ("Request failed")



if __name__ == '__main__':
    print(weather_forecast("pearl mississippi"))