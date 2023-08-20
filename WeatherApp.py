import requests
import json
import win32com.client as wincom
city = input("Enter the name of city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=82e0179635dd4d5fa39144842231105&q={city}"
r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
x = wdic["current"]["condition"]["text"]
y = wdic["current"]["humidity"]
speak = wincom.Dispatch("SAPI.SpVoice")
text = f"the current temperature in {city} is {w} degree celcius, the weather condition is {x}, the humidity is {y} percent"
speak.Speak(text)
