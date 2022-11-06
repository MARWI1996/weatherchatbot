"""
Custom actions implemented in Python used for the weather forecast chatbot
The slots and responses are exchanged with RASA here
Here the weather data is retrieved and the responses for enquiring the weather are created
"""

# Import of libraries
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from weather_data import request_info_city


class Weather(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Retrieve the current slots from RASA
        city = tracker.get_slot('city')
        weather_type = tracker.get_slot('weather_type')
        forec_period = tracker.get_slot('forec_period')

        # Empty slots
        if forec_period is None:
            forec_period = "current"
        if weather_type is None:
            weather_type = "weather"

        # set the forecast steps for OpenWeather forecast json format
        day = 0
        if forec_period == "tomorrow":
            day = 1

        # list possible cities
        allowed_cities = ["Bregenz", "Innsbruck", "Salzburg", "Linz", "Graz", "Klagenfurt", "St. Pölten", "Eisenstadt",
                          "Vienna"]

        # Default answer
        response = "I am sorry, I could not find that information - I hope it is going to be nice weather. "

        # read information and generate response
        if city in allowed_cities:

            # get the weather information from function defined in weather_data.py
            open_wx_msg = request_info_city(city)

            # set values to current weather
            temp = round(open_wx_msg['current']['temp'])
            pressure = round(open_wx_msg['current']['pressure'])
            humidity = round(open_wx_msg['current']['humidity'])
            wind = round(open_wx_msg['current']['wind_speed'])
            wind_deg = round(open_wx_msg['current']['wind_deg'])
            cond = (open_wx_msg['current']['weather'][0]["description"])
            uvi = (open_wx_msg['current']['uvi'])

            # set values to forecasted weather
            temp_min_predict = round(open_wx_msg['daily'][day]['temp']['min'])
            temp_max_predict = round(open_wx_msg['daily'][day]['temp']['max'])
            pressure_predict = round(open_wx_msg['daily'][day]['pressure'])
            humidity_predict = round(open_wx_msg['daily'][day]['humidity'])
            wind_speed_predict = round(open_wx_msg['daily'][day]['wind_speed'])
            wind_deg_predict = round(open_wx_msg['daily'][day]['wind_deg'])
            cond_predict = (open_wx_msg['daily'][day]['weather'][0]["description"])
            uvi_predict = round(open_wx_msg['daily'][day]['uvi'])
            rain_predict = round(open_wx_msg['daily'][day]['rain'], 1)

            # answers to queries about current weather
            if forec_period == 'current':
                # general answer
                if weather_type == 'weather':
                    response = "The current temperature in {} is {}°C. It is {} and the wind speed is {}m/s".format(
                        city,
                        temp,
                        cond,
                        wind)
                # specific information
                if weather_type == 'wind':
                    response = "The current wind speed in {} is {} metres per second from {} degrees. ".format(city,
                                                                                                               wind,
                                                                                                               wind_deg)
                if weather_type == 'temperature':
                    response = "The current temperature in {} is {}°C. ".format(city, temp)
                if weather_type == 'pressure':
                    response = "The current air pressure in {} is {} millibars. ".format(city, pressure)
                if weather_type == 'humid':
                    response = "The current humidity in {} is {}%. ".format(city, humidity)
                if weather_type == 'uvi':
                    response = "The current UV index in {} is {}. ".format(city, uvi)
                if weather_type == 'cloud_conditions':
                    response = "The current conditions in {} is {}.".format(city, cond)

            # answers to forecasts for today and tomorrow
            if forec_period == 'today' or forec_period == 'tomorrow':
                # general answer
                if weather_type == 'weather':
                    response = "The forecast high for {} {} is {}°C. It is expected to be {} and the wind speed is {}m/s".format(
                        city, forec_period, temp_max_predict, cond_predict, wind_speed_predict)
                # more specific forecasts
                if weather_type == 'wind':
                    response = "The forecasted wind speed for {} {} is {} metres per second from {} degrees. ".format(
                        city, forec_period, wind_speed_predict, wind_deg_predict)
                if weather_type == 'temperature':
                    response = "The forecasted maximum temperature for {} {} is {}C while the minimum is {}°C. ".format(
                        city, forec_period, temp_max_predict, temp_min_predict)
                if weather_type == 'pressure':
                    response = "The forecasted air pressure for {} {} is {} millibars. ".format(city, forec_period,
                                                                                                pressure_predict)
                if weather_type == 'humid':
                    response = "The forecasted humidity for {} {} is {}%. ".format(city, forec_period,
                                                                                   humidity_predict)
                if weather_type == 'uvi':
                    response = "The forecasted UV index for {} {} is {}. ".format(city, forec_period, uvi_predict)
                if weather_type == 'cloud_conditions':
                    response = "The predicted conditions for {} {} is {} and 24hrs rain fall is expected to be {}mm".format(
                        city, forec_period, cond_predict, rain_predict)


        # response if information about none Austrian capital is asked
        else:
            response = "Sorry, I am currently limited to weather information of Austrian capitals only"

        # send the response back to RASA
        dispatcher.utter_message(response)
