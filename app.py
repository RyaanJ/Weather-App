import requests
#Api key for weather data
api_key = '6cc09a272714e86c3fb04962c7ef8811'

user_input = input("Enter City: ")
#finds all data given city and api key
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
#Error Handling, if city name is typed incorrect, will ask again until a correct city is given
while weather_data.json()['cod'] == '404':
    print("No City Found with this name")
    user_input = input("Try entering a city again: ")
    #After correct city is given, line below gives weather data to go through to the else:
    weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
else: 
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    temp_in_celsius = round((temp - 32) * 5/9)

    print(f"The weather in {user_input} is: {weather}.")
    print(f"The temperature in {user_input} is: {temp_in_celsius} celsius or {temp} fahrenheit.")