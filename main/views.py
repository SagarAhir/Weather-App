from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):

    if request.method == 'POST':
        city = request.POST['city']
        
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=ec90b5cac62a2c858e6ce157b8b8799d').read()

        json_data = json.loads(source)
        # print(json_data)

        kelvin = json_data['main']['temp']
        celsius = round(kelvin - 273.15,2)
        data = {
            "city": str(json_data['name']),
            "coord": str(json_data['coord']['lon']) +', '+ str(json_data['coord']['lat']),
            "temp": str(celsius) + ' °C',
            "humidity": str(json_data['main']['humidity']),
            "pressure": str(json_data['main']['pressure']),
            "wind_speed": str(json_data['wind']['speed']),
            "wind_degree": str(json_data['wind']['deg']),
        }

        # print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)