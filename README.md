# WeatherBob
In collaboration with Henri Haukipuro and Valtteri Impola as a part of a school course


# Description
WeatherBob is a Python3-based software which uses OpenWeatherMap-API combined with Telegram bot -API. By sending a city name to the Telegam bot the bot returns basic weather data for the given city

![alt text](https://user-images.githubusercontent.com/32328856/47872742-0d636800-de18-11e8-8f27-e0544affa7bd.png)

# How does it work?
After the user has sent the city name to the Telegram bot, the data for the given city is parsed down to a basic weather information level (Name of the city, temperature, wind speed and the dominant state of the weather) and gets sent back to the user. The city name is checked whether it exists or not by looping all the available city names from a pre-existing list (city_list.json).

**Flowchart**

![](https://user-images.githubusercontent.com/32328856/48059772-c92ee980-e1c2-11e8-99ab-2aa856627449.png)
