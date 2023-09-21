import requests
import json
import pyttsx3

city = input("Enter the name of the city\n")
url ="https://api.weatherapi.com/v1/current.json?key=894362ef73d14bfa93c135754232009&q={city}"

r = requests.get(url)
engine = pyttsx3.init()
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

engine.say(city)
engine.say(w)

engine.runAndWait()