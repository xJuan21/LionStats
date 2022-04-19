from email import utils
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from urllib import request
from django.shortcuts import render
import os
import webbrowser 
import time 

def delete_product(request):
    if request.method == "GET":
        url = ' http://127.0.0.1:7000/' 
        chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s' 
        webbrowser.get(chrome_path).open(url) 
        os.system("cd utils && py authorization.py runserver")
        
        return render(request, "dashboard.html")
      
class TeamData(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        labels = ["DIST", "HR90"]
        teamData = [5000, 15]
        data = {
            "labels": labels,
            "default": teamData,
        }
        return Response(data)

