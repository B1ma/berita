from django.http import HttpResponse
from django.shortcuts import render
import requests


def homepage(request, **kwargs):
    template_name = "front/homepage.html"
    
    URL = "https://the-lazy-media-api.vercel.app/api/games?page=1"
    
    r = requests.get(url = URL)
    
    data = r.json()
    

    context = {
        'data':data,
        'data1':data[0],
        'data2':data[1],
        'data3':data[2],
        
        }


    return render(request, template_name, context)


def detail_page(request, id, **kwargs):
    template_name = "front/page.html"

    return render(request, template_name)

def hotnews(request):
    template_name = "front/hotnews.html"

    return render(request, template_name)

def contact(request):
    template_name = "front/contact.html"

    return render(request, template_name)

def author(request):
    template_name = "front/author.html"

    return render(request, template_name)
