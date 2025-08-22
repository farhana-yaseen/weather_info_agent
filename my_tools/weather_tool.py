from agents import function_tool
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Weather tool
@function_tool
def get_weather(city:str):
   
    """
    Get real-time weather for a given city using WeatherAPI.com.
    """

    weather_api = os.getenv("WEATHER_API_KEY")
   
    if not weather_api:
        return "API key not found. Please set the WEATHER_API_KEY environment variable."

    url = f"http://api.weatherapi.com/v1/current.json?key={weather_api}&q={city}&aqi=no"
    

    try:
        # fetch the weather data.
        response = requests.get(url)

        # Handles errors
        response.raise_for_status()

        # get data in json format
        data = response.json()

        location = data["location"]["name"]
        country = data['location']['country']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']

        return f"The weather in {location}, {country} is '{condition}' with a temperature of {temp_c}°C."
   
    except requests.RequestException as e:
        return f"Request failed: {e}"
    except KeyError:
        return "Unexpected response format from WeatherAPI."



    # return f"The weather in {location}, {country} is '{condition}' with a temperature of {temp_c}°C."
    
  
    


