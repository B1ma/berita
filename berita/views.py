from django.http import HttpResponse
from django.shortcuts import render
from artikels.models import *
import requests
import random


def sinkron_game(request):
    URL = "https://the-lazy-media-api.vercel.app/api/games?page=1"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    for d in data:
        cek_game = Gamesartikels.objects.filter(key=d['key'])
        if cek_game.exists():
            game = cek_game.first()
            game.title = d['title']
            game.thumb = d['thumb']
            game.date = d['time']
            game.desc = d['desc']
            game.key = d['key']
        else:
            Gamesartikels.objects.create(
                title = d['title'],
                thumb = d['thumb'],
                date = d['time'],
                desc = d['desc'],
                key = d['key'],
                
            )
    return HttpResponse("<h1>Berhasil connect API</h1>")

def homepage(request):
    template_name = "front/homepage.html"
    
    data = Gamesartikels.objects.all()

    context = {
        'data':data,
        'data1':data[0],
        'data2':data[1],
        'data3':data[2],
        
        }


    return render(request, template_name, context)


def detail_page(request, key):
    template_name = "front/page.html"
    
    URL = "https://the-lazy-media-api.vercel.app/api/detail/{}".format(key)
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    data1 = Gamesartikels.objects.all()
    
    list1 = [1, 2, 3, 4, 5]
    
    context = {
        'data' : data['results'],
        'gambar' : data['results']['content'][0],
        'figure' : data['results']['figure'],
        'data1':data1[random.choice(list1)],
        'data2':data1[random.choice(list1)],
    }

    return render(request, template_name, context)

def hotnews(request):
    template_name = "front/hotnews.html"

    return render(request, template_name)

def contact(request):
    template_name = "front/contact.html"

    return render(request, template_name)

def about(request):
    template_name = "front/about_us.html"

    return render(request, template_name)

def author(request):
    template_name = "front/author.html"

    return render(request, template_name)
