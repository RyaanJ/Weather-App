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


user_input2 = input("Would you like the temperate in Celsius or Fahrenheit?: ")
while (user_input2 != "Celsius") or (user_input2 != "Fahrenheit"):
    print("Oops, try typing that again")
    user_input2 = input("Please choose one, Celsius or Fahrenheit?: ")
    if (user_input2 == "Celsius") or (user_input2 == "Fahrenheit"):
        break

if user_input2 == "Celsius":
    print(f"The weather in {user_input} is: {weather}.")
    print(f"The temperature in {user_input} is {temp_in_celsius} degrees Celsius.")
elif user_input2 == "Fahrenheit":
    print(f"The weather in {user_input} is: {weather}.")
    print(f"The temperature in {user_input} is {temp} degrees Fahrenheit.")
