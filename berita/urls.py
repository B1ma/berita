from django.contrib import admin
from django.urls import path, re_path, include

from berita.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage, name="homepage"),
    path('hotnews/',hotnews, name="hotnews"),
    path('contact/',contact, name="contact"),
    path('author/',author, name="author"),
    path("sinkron_games/", sinkron_game, name="sinkrongame"),
    path("page/<path:key>",detail_page, name="detail"),
    path('about/',about, name="about"),
    # apps
    path("dashboard/", include("artikels.urls"))
    
]
