import requests
from decimal import *

class Weather:

    def get_weather(self ,city):
        """
        This method reaches out to the openweathermap API and returns
        a dictionary of all weather related data
        """

        self.city = city
        API_KEY = "2ae4c3cf7b4ff33f6151287d90ca1771"
        URL = "https://api.openweathermap.org/data/2.5/weather?"
        self.parameters= {"appid": API_KEY, "q": self.city }
        try:
            self.response = requests.get(URL, params=self.parameters)
            self.weather_data = self.response.json()

        except request.exceptions.ConnectionError as err:
            return "Connection error, request could not be made!"
            
        return self.weather_data

    def format_data(self, data):
        """
        This method collects the API data as input and pulls out relevant information from it
        """

        def K_to_celcius(temp):
            kelvin = float(temp)
            celsius = kelvin - 273.15
            rounded_celcius = round(celsius, 1) # rounds it into a nicer number for display
            return rounded_celcius

        self.data = data
        temp_in_k = K_to_celcius(self.data["main"]["temp"]) 
        weather_description = self.data["weather"][0]["description"]

        return_data = {
            "temprature": temp_in_k,
           "weather_description" : weather_description
        }
       # print(return_data)
        return return_data
       

  



