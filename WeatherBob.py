
# Imports for json handling and other stuff.
import requests
import json
import datetime
import time
from datetime import datetime
currentDateTime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def naytaSaa(city):
    global d
    kaupunki = city
    loytyyko = False
    file = open("/home/pi/city.list.json") # <- Specify your path to city.list.json here. It can be downloaded from the repository.
    with file as json_data:
        
        
        d = json.load(json_data) # Load the contents of city.list to a variable.
        file.close() # Close the file when reading is done.
        lista = len(d) # Store the length of city.list array to a variable.
    
    for i in range (0, lista): # Compare the given city name to the array if it's there
        if(d[i]["name"] == kaupunki):
            print("löytyy")             
            loytyyko = True # If the given city name exists, stop the for-loop and proceed to if-statement.
            break
                    
    if(loytyyko == True):
    
        url =  requests.get("http://api.openweathermap.org/data/2.5/weather?q="+kaupunki+"&APPID={INSERT YOUR OPENWEATHERMAP API-KEY HERE}") # Read the contents of the given city name from the OpenWeatherMap API.
        data = json.loads(url.text) # Store the contents to a variable.
        celcius = data["main"]["temp"] - 273.15 # Temperature conversions.
        windSpeed = "wind speed: " + str(data["wind"]["speed"]) + " m/s" # Query from json.
        name = data["name"] # Query from json.
        temperature = ("Temperature: " + "%.2f" % celcius + " °C") # Query from json.
        description = data["weather"][0]["description"] # Query from json.
    
        # Print and return data.
        print(name)
        print(temperature)
        print(description)
        print(windSpeed)
        print(currentDateTime)
        return name, currentDateTime, temperature, description, windSpeed

    else:
        return kaupunki + " Ei löytynyt listalta. Huomioi iso alkukirjain ja oikeinkirjoitus." # Given city name not found. Return an error message.


TOKEN = "INSERT YOUR TELEGRAM API-KEY HERE" # Token of the Telegram bot.
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def getUrl(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def getJSONFromURL(url):
    content = getUrl(url)
    js = json.loads(content)
    return js

def getUpdates():
    url = URL + "getUpdates"
    js = getJSONFromURL(url)
    return js

def getLastChatIdAndtext(updates):
    numUpdates = len(updates["result"])
    lastUpdate = numUpdates -1
    text = updates["result"][lastUpdate]["message"]["text"]
    chatID = updates["result"][lastUpdate]["message"]["chat"]["id"]
    return(text, chatID)

def sendMessage(text, chatID):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chatID)
    getUrl(url)

def main():
    last_textchat = (None, None)
    while True:
        text, chat = getLastChatIdAndtext(getUpdates())
        if (text, chat) != last_textchat:
            sendMessage(naytaSaa(text), chat)
            last_textchat = (text, chat)
        time.sleep(0.5)
    
if __name__== '__main__':
    
    main()
        




