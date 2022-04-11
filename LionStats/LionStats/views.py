from urllib import request
#import mypythoncode
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.shortcuts import render
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



def delete_product(request):
    if request.method == "GET":
        print("hola delete")
        return render(request, "dashboard.html")

