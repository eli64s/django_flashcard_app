"""gre_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# This file serves the purpose to route urls to views

from django.conf.urls import url, include
from django.contrib import admin
from . import views # . means we are in the same directory (views is in same directory as urls)

# r - raw text
# ^ - start at this string
urlpatterns = [ 

    # Index url - Maps an empty url string such as 'localhost:8000' to the home function in views.py
    url(r'^$', views.index, name = 'index'), 
    url(r'^admin/', admin.site.urls), 
    url(r'^flashcards/', include(('flashcards.urls', 'flashcards'), namespace = 'flashcards')),
]
