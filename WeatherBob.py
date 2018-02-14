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
    file = open("/home/pi/city.list.json")
    with file as json_data:
        
        d = json.load(json_data)
        file.close()
        lista = len(d)
    
    for i in range (0, lista):
        if(d[i]["name"] == kaupunki):
            print("löytyy")             
            loytyyko = True
            break
                    
    if(loytyyko == True):
    
        url =  requests.get("http://api.openweathermap.org/data/2.5/weather?q="+kaupunki+"&APPID={INSERT YOUR OPENWEATHERMAP API-KEY HERE}")
        data = json.loads(url.text)
        celcius = data["main"]["temp"] - 273.15
        windSpeed = "wind speed: " + str(data["wind"]["speed"]) + " m/s"
        name = data["name"]
        temperature = ("Temperature: " + "%.2f" % celcius + " °C")
        description = data["weather"][0]["description"]
    
        print(name)
        print(temperature)
        print(description)
        print(windSpeed)
        print(currentDateTime)
        return name, currentDateTime, temperature, description, windSpeed

    else:
        return kaupunki + " Ei löytynyt listalta. Huomioi iso alkukirjain ja oikeinkirjoitus."


TOKEN = "INSERT YOUR TELEGRAM API-KEY HERE" #botin token, pitää poistaa ennen ku laittaa gittiin
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
        




