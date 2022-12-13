from django.contrib import admin
from django.urls import path

from berita.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage, name="homepage"),
    path('hotnews/',hotnews, name="hotnews"),
    path('contact/',contact, name="contact"),
    path('author/',author, name="author"),
    path("page/<slug:key>",detail_page, name="detail")
    
]
