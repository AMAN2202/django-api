import requests
from django.shortcuts import render,redirect
from weather.models import  Cities
from weather.forms import  CityForm
from django.contrib import messages
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&unit=Metric&appid=fea505f0d2b530b55fc08802904a4177'


# Create your views here.
def home(request):
    we=[]
    if request.method=='POST':
        form=CityForm(request.POST)
        if form.is_valid():
            form.save()
    for city in Cities.objects.all():
        r=requests.get(url.format(city)).json()
        if(r['cod']==200):
            city_w={
                'city': city,
                'temp': r['main']['temp'],
                'clouds': r['clouds']['all'],
                'weather': r['weather'][0]['description'],
                'temp_min': r['main']['temp_min'],
                'temp_max': r['main']['temp_max'],
            }
            we.append(city_w)
    form=CityForm()
    context={'we':we,'form':form}
    return render(request,'home.html',context)