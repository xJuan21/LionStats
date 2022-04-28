import os
import subprocess
import sys
import webbrowser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from teamproAPI import teampro_queries
from teamproAPI import authorization


def delete_product(request):
    if request.method == "GET":
        url = 'http://127.0.0.1:8080/'
        browser_path = 'open -a /Applications/Chrome.app %s'
        firefox_path = '"C:/Program Files/Mozilla Firefox/firefox.exe" %s'
        #webbrowser.get(browser_path).open(url, new=2)
        webbrowser.open(url, new=2, autoraise=True)
        # if getattr(sys, 'frozen', False):
        #      app_path = os.path.dirname(sys.executable)
        #      os.chdir(app_path)
        #      os.system("cd teamproAPI && py authorization.py runserver")
        # else:
        #     os.system("cd teamproAPI && py authorization.py runserver")

        authorization.main()
        #authorization.setup()
        authorization.authorize()
        authorization.callback()

        return render(request, "dashboard.html")

def getData(request):
    global team_name
    team_name = request.POST.get('value')
    print(team_name)
    return HttpResponse(team_name)

def getStartDate(request):
    global startDate
    startDate = request.POST.get('value')
    return HttpResponse(startDate)

def getEndDate(request):
    global endDate
    endDate = request.POST.get('value')
    return HttpResponse(endDate)


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
        teampro_queries.TeamProExample.__init__(self)
        dropData = teampro_queries.TeamProExample.get_teams(self)

        return Response(dropData)


# class GetData(APIView):
#
#     def get(self, request):
#         dataT = request.GET.get('value', "")
#         return Response(dataT)
#
#     # def post(self, request):
#     #     dataT = request.POST.get('value', "")
#     #     return Response(dataT)

class TeamDetails(APIView):

    def get(self, request, format=None):

        # name = self.getTeams(request)
        # print(name)
        # name = self.data(request)
        # print(name)
        # name = getData(request).teamName;
        teampro = teampro_queries.TeamProExample()
        teamDetails = teampro.get_team_details(team_name)
        return Response(teamDetails)

class TeamSessionDate(APIView):

    def get(self, request, format=None):

        strEndDate = str(endDate)
        strStartDate = str(startDate)
        print(strStartDate)
        print(strEndDate)
        teampro = teampro_queries.TeamProExample()
        teamSessions = teampro.get_session_dates_from_timeframe(team_name, strStartDate, strEndDate)
        return Response(teamSessions)

class TeamMetrics(APIView):

    def get(self,request, format=None):
        teampro = teampro_queries.TeamProExample()
        teamID = teampro.get_team_id(team_name)
        strEndDate = str(endDate)
        strStartDate = str(startDate)
        teamMetrics = teampro.get_team_metrics_by_date(teamID, strStartDate, strEndDate)

        return Response(teamMetrics)
