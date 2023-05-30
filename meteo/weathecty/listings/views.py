# le ficher views.py permet de recevoir des requetes et avoir des reponses
# il permet aussi d'interagir avec la base de donnée et des requetes ainsi que les templates 

from django.shortcuts import render
import requests
import datetime

def index(request):
    if 'ville' in request.POST:
        ville = request.POST['ville']
    else:
        ville = 'Paris'
    appid = '3c6dbf0dbebcf67f23f493c1dae4e3f8'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMETRE = {'q': ville, 'appid': appid, 'units': 'metric'}
    
    r = requests.get(url=URL, params=PARAMETRE)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    temp_min = res ['main']['temp_min']
    temp_max = res ['main']['temp_max']
    humidity = res['main']['humidity']

    day = datetime.date.today()

    return render(request, 'listings/index.html', {'description': description, 'icon': icon, 'temp': temp, 'humidity': humidity, 'day': day, 'ville': ville, 'temp_min':temp_min, 'temp_max':temp_max})

