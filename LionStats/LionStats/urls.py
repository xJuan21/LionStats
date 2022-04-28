"""LionStats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from LionStats import views
from .views import *


def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def summary(request):
    return render(request, 'summary.html')

def individual(request):
    return render(request, 'individual.html')

def comparison(request):
    return render(request, 'comparison.html')

def team(request):
    return render(request, 'team-filter.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('dashboard/', dashboard),
    path('summary/', summary),
    path('individual/', individual),
    path('comparison/', comparison),
    path('team/', team),
    path('api/dropdown/', Dropdown.as_view()),
    path('api/team/data/', TeamData.as_view()),
    path('api/dropdown/team', TeamDetails.as_view()),
    path('api/dropdown/sessions', TeamSessionDate.as_view()),
    path('api/metrics', TeamMetrics.as_view()),
    path('delete_product', views.delete_product, name='delete_product'),
    path('JSendpoint/', views.getData, name='getData'),
    path('startdate/', views.getStartDate, name='startdate'),
    path('enddate/',views.getEndDate, name='enddate'),
]

urlpatterns += staticfiles_urlpatterns()
