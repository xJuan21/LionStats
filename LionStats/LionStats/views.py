import os
import webbrowser

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from urllib import request
from django.shortcuts import render
from teamproAPI import teampro_test

def delete_product(request):
    if request.method == "GET":
        url = 'http://127.0.0.1:8080/'
        chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
        firefox_path = "open -a /Applications/Chrome.app %s"
        webbrowser.get(firefox_path).open('http://127.0.0.1:8080/')
        os.system("cd teamproAPI && python authorization.py runserver")

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


class Dropdown(APIView):

    def get(self, request, format=None):
        teampro_test.TeamProExample.__init__(self)
        dropData = teampro_test.TeamProExample.get_teams(self)

        return Response(dropData)


class TeamDetails(APIView):

    def get(self, request, format=None):
        name = request.POST.get('dropdown', False)
        teampro = teampro_test.TeamProExample()
        teamID = teampro.get_team_id("Women's Lacrosse")
        teamDetails = teampro.get_team_details(teamID)
        return Response(teamDetails)

