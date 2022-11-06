"""
Python code for returning weather data depending on the requested city
The weather data is static defined and not connected to any database or API for retrieving real weather data
The Austrian capitals: Bregenz, Innsbruck, Salzburg, Klagenfurt, St. Pölten, Graz, Linz, Eisenstadt
and Vienna can be requested.
"""


def request_info_city(city):
    """
    Function for returning the weather data of the requested city
    """

    if city == "Bregenz":
        weather_data = {'current': {'temp': 20.13, 'pressure': 1014, 'humidity': 61, 'uvi': 8.34, 'wind_speed': 1.79,
                                    'wind_deg': 206, 'weather': [{'description': 'clear sky'}], 'rain': 0.00},
                        'daily': [{'temp': {'min': 14.82, 'max': 21.78},
                                   'pressure': 1015, 'humidity': 50, 'wind_speed': 4.36, 'wind_deg': 241,
                                   'weather': [{'description': 'scattered clouds'}], 'rain': 0.29, 'uvi': 12.22},
                                  {'temp': {'min': 15.45, 'max': 24.08},
                                   'pressure': 1017, 'humidity': 58, 'wind_speed': 3.18, 'wind_deg': 341,
                                   'weather': [{'description': 'light rain'}], 'rain': 0.29, 'uvi': 7.95}]}

    if city == "Innsbruck":
        weather_data = {'current': {'temp': 19.65, 'pressure': 1024, 'humidity': 46, 'uvi': 9.34, 'wind_speed': 2.62,
                                    'wind_deg': 271, 'weather': [{'description': 'cloudy'}], 'rain': 0.00},
                        'daily': [{'temp': {'min': 08.62, 'max': 19.98},
                                   'pressure': 1016, 'humidity': 51, 'wind_speed': 2.26, 'wind_deg': 281,
                                   'weather': [{'description': 'rainy'}], 'rain': 1.43, 'uvi': 11.56},
                                  {'temp': {'min': 08.11, 'max': 18.45},
                                   'pressure': 1018, 'humidity': 57, 'wind_speed': 3.78, 'wind_deg': 331,
                                   'weather': [{'description': 'rainy'}], 'rain': 0.78, 'uvi': 9.63}]}

    if city == "Salzburg":
        weather_data = {'current': {'temp': 18.73, 'pressure': 1044, 'humidity': 49, 'uvi': 9.78, 'wind_speed': 6.67,
                                    'wind_deg': 259, 'weather': [{'description': 'scattered clouds'}], 'rain': 0.20},
                        'daily': [{'temp': {'min': 09.78, 'max': 20.68},
                                   'pressure': 1047, 'humidity': 54, 'wind_speed': 7.36, 'wind_deg': 277,
                                   'weather': [{'description': 'clear sky'}], 'rain': 0.00, 'uvi': 10.78},
                                  {'temp': {'min': 09.87, 'max': 20.21},
                                   'pressure': 1023, 'humidity': 58, 'wind_speed': 6.18, 'wind_deg': 321,
                                   'weather': [{'description': 'clear sky'}], 'rain': 0.00, 'uvi': 10.98}]}

    if city == "Klagenfurt":
        weather_data = {'current': {'temp': 17.65, 'pressure': 1021, 'humidity': 42, 'uvi': 10.65, 'wind_speed': 3.18,
                                    'wind_deg': 265, 'weather': [{'description': 'sunny'}], 'rain': 0.0},
                        'daily': [{'temp': {'min': 08.56, 'max': 17.69},
                                   'pressure': 1056, 'humidity': 45, 'wind_speed': 6.21, 'wind_deg': 289,
                                   'weather': [{'description': 'clear sky'}], 'rain': 0.00, 'uvi': 11.89},
                                  {'temp': {'min': 07.89, 'max': 17.57},
                                   'pressure': 1049, 'humidity': 42, 'wind_speed': 5.21, 'wind_deg': 312,
                                   'weather': [{'description': 'clear sky'}], 'rain': 0.00, 'uvi': 11.65}]}

    if city == "Graz":
        weather_data = {'current': {'temp': 16.21, 'pressure': 1056, 'humidity': 78, 'uvi': 07.12, 'wind_speed': 1.56,
                                    'wind_deg': 156, 'weather': [{'description': 'foggy'}], 'rain': 5.2},
                        'daily': [{'temp': {'min': 09.12, 'max': 18.65},
                                   'pressure': 1035, 'humidity': 47, 'wind_speed': 5.63, 'wind_deg': 176,
                                   'weather': [{'description': 'sunny'}], 'rain': 0.00, 'uvi': 13.12},
                                  {'temp': {'min': 8.12, 'max': 17.68},
                                   'pressure': 1065, 'humidity': 68, 'wind_speed': 2.61, 'wind_deg': 198,
                                   'weather': [{'description': 'rainy'}], 'rain': 7.32, 'uvi': 11.65}]}

    if city == "Linz":
        weather_data = {'current': {'temp': 17.11, 'pressure': 1036, 'humidity': 42, 'uvi': 11.68, 'wind_speed': 2.45,
                                    'wind_deg': 256, 'weather': [{'description': 'clear sky'}], 'rain': 0.0},
                        'daily': [{'temp': {'min': 11.36, 'max': 20.32},
                                   'pressure': 1025, 'humidity': 42, 'wind_speed': 1.98, 'wind_deg': 276,
                                   'weather': [{'description': 'sunny'}], 'rain': 0.00, 'uvi': 12.35},
                                  {'temp': {'min': 10.35, 'max': 19.78},
                                   'pressure': 1025, 'humidity': 41, 'wind_speed': 1.65, 'wind_deg': 281,
                                   'weather': [{'description': 'sunny'}], 'rain': 0.00, 'uvi': 12.15}]}

    if city == "Eisenstadt":
        weather_data = {'current': {'temp': 16.32, 'pressure': 1089, 'humidity': 51, 'uvi': 10.32, 'wind_speed': 4.68,
                                    'wind_deg': 216, 'weather': [{'description': 'cloudy'}], 'rain': 0.0},
                        'daily': [{'temp': {'min': 09.48, 'max': 18.69},
                                   'pressure': 1087, 'humidity': 49, 'wind_speed': 3.54, 'wind_deg': 221,
                                   'weather': [{'description': 'clear sky'}], 'rain': 0.00, 'uvi': 13.15},
                                  {'temp': {'min': 10.35, 'max': 19.78},
                                   'pressure': 1081, 'humidity': 47, 'wind_speed': 2.98, 'wind_deg': 227,
                                   'weather': [{'description': 'clear sky'}], 'rain': 0.00, 'uvi': 13.89}]}

    if city == "Vienna":
        weather_data = {'current': {'temp': 15.18, 'pressure': 1046, 'humidity': 45, 'uvi': 08.21, 'wind_speed': 15.32,
                                    'wind_deg': 216, 'weather': [{'description': 'stormy'}], 'rain': 0.0},
                        'daily': [{'temp': {'min': 10.12, 'max': 19.77},
                                   'pressure': 1032, 'humidity': 41, 'wind_speed': 2.15, 'wind_deg': 189,
                                   'weather': [{'description': 'sunny'}], 'rain': 0.00, 'uvi': 13.25},
                                  {'temp': {'min': 10.35, 'max': 19.78},
                                   'pressure': 1036, 'humidity': 45, 'wind_speed': 2.78, 'wind_deg': 187,
                                   'weather': [{'description': 'sunny'}], 'rain': 0.00, 'uvi': 13.77}]}

    if city == "St. Pölten":
        weather_data = {'current': {'temp': 17.56, 'pressure': 1066, 'humidity': 52, 'uvi': 11.23, 'wind_speed': 03.12,
                                    'wind_deg': 223, 'weather': [{'description': 'sunny'}], 'rain': 0.0},
                        'daily': [{'temp': {'min': 08.21, 'max': 17.12},
                                   'pressure': 1044, 'humidity': 41, 'wind_speed': 2.98, 'wind_deg': 226,
                                   'weather': [{'description': 'rainy'}], 'rain': 10.21, 'uvi': 08.21},
                                  {'temp': {'min': 07.35, 'max': 16.21},
                                   'pressure': 1051, 'humidity': 45, 'wind_speed': 2.78, 'wind_deg': 228,
                                   'weather': [{'description': 'rainy'}], 'rain': 11.11, 'uvi': 07.89}]}

    return weather_data
