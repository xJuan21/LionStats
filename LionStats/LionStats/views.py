import os
import subprocess
import json
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
    return HttpResponse(team_name)

def getStartDate(request):
    global startDate
    startDate = request.POST.get('value')
    return HttpResponse(startDate)

def getEndDate(request):
    global endDate
    endDate = request.POST.get('value')
    return HttpResponse(endDate)

def getSession(request):
    global session
    session = request.Post.get('value')
    return HttpResponse(session)

def getAthlete(request):
    global athletes
    global firstName
    global lastName
    athletes = []
    athletes.append(request.POST.getlist('value[]'))

    list = str(athletes[0]).split(',')
    first, lastName, position = list[0].split(' ')

    junk, firstName = first.split("'")
    # firstName, lastName = athletes.split(" ", 2)

    return HttpResponse(athletes)


class Metrics:

    def metrics(self):
        teampro = teampro_queries.TeamProExample()
        team_id = teampro.get_team_id(team_name)
        player_id = teampro.get_player_id(team_name, firstName, lastName)
        metrics = teampro.get_individual_metrics_by_date(team_id, player_id, startDate, endDate)
        # metricsJson = json.loads(metrics)
        # metricsList = []
        # for i in range(1, metricsJson.length):
        #    metricsList.append(i)
        # print(metrics)

        return metrics

class TeamData(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """

        teampro = teampro_queries.TeamProExample()
        playerID = teampro.get_player_id(team_name, firstName, lastName)
        print(playerID)
        metrics = Metrics.metrics(self)
        print(metrics)
        for item in metrics['players']:
            if item['player_id'] == playerID:
                print()


        labels = ["Duration",
                    "eTrimp",
                    "sTrimp",
                    "EXP",
                    "HR90",
                    "DIST",
                    "HSR",
                    "SPNT",
                    "HSR/SP",
                    "rEXP",
                    "rDIST",
                    "rHSR" ,
                    "rSPNT"]
        teamData = [5, 5, 1, 2, 4, 8, 8, 1, 5, 4, 6, 7, 9]
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

        teampro = teampro_queries.TeamProExample()
        teamSessions = teampro.get_session_dates_from_timeframe(team_name, strStartDate, strEndDate)
        return Response(teamSessions)

# class TeamMetrics(APIView):
#
#     def get(self,request, format=None):
#         teampro = teampro_queries.TeamProExample()
#         teamID = teampro.get_team_id(team_name)
#         strEndDate = str(endDate)
#         strStartDate = str(startDate)
#         # teamMetrics = teampro.get_team_metrics_by_date(teamID, strStartDate, strEndDate)
#         playerID = teampro.get_player_id(teamID, firstName, lastName)
#         print(playerID)
#         return Response(playerID)
