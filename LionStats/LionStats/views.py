import json
import webbrowser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render
from teamproAPI import teampro_queries
from teamproAPI import authorization

# Login redirect function
def delete_product(request):
    if request.method == "GET":
        # redirect to this url
        url = 'http://127.0.0.1:8080/'
        #open new tab in default browser
        webbrowser.open(url, new=2, autoraise=True)

        #run 3 main functions from authorization file in order to authenticate login
        authorization.main()
        authorization.authorize()
        authorization.callback()

        #render page
        return render(request, "dashboard.html")

#get the team name from the POST request done by Javascript function
def getData(request):
    global team_name
    team_name = request.POST.get('value')
    return HttpResponse(team_name)

#get the start date value from the POST request done by Javascript function
def getStartDate(request):
    global startDate
    startDate = request.POST.get('value')
    return HttpResponse(startDate)

#get the end date value from the POST request done by Javascript function
def getEndDate(request):
    global endDate
    endDate = request.POST.get('value')
    return HttpResponse(endDate)

#get the session value from the POST request done by Javascript function
def getSession(request):
    global session
    session = request.POST.get('value')
    return HttpResponse(session)

#get the athlete name from the POST request done by Javascript function
def getAthlete(request):
    global athletes
    global firstName
    global lastName
    athletes = []
    #append the string returned from the POST request to an array
    athletes.append(request.POST.getlist('value[]'))

    #split up the string into 3 seperate variables
    list = str(athletes[0]).split(',')
    first, lastName, position = list[0].split(' ')
    junk, firstName = first.split("'")

    return HttpResponse(athletes)

#get the summary of the metrics for the home page
class HomeMetrics:

    def get(self, request, format=None):
        teampro = teampro_queries.TeamProExample()
        teamID = teampro.get_team_id(team_name)
        homeMetrics = teampro.get_home(teamID)
        summary = teampro.summarize_by_day(homeMetrics)
        return summary

#create the data to be passed to the chart on the individual page
class Metrics(APIView):

    def get(self, request, format=None):
        teampro = teampro_queries.TeamProExample()
        team_id = teampro.get_team_id(team_name)
        player_id = teampro.get_player_id(team_name, firstName, lastName)
        metrics = teampro.get_individual_metrics_by_date(team_id, player_id, startDate, endDate)
        summary = teampro.summarize_by_day(metrics)

        metrics = []
        data = HomeMetrics.get(self, request)

        print(data)
        #append each specific metric to the array for the chart data
        metrics.append(data['metrics'][0]['Duration'])
        metrics.append(data['metrics'][0]['eTrimp'])
        metrics.append(data['metrics'][0]['sTrimp'])
        metrics.append(data['metrics'][0]['EXP'])
        metrics.append(data['metrics'][0]['HR90'])
        metrics.append(data['metrics'][0]['DIST'])
        metrics.append(data['metrics'][0]['HSR'])
        metrics.append(data['metrics'][0]['SPNT'])
        metrics.append(data['metrics'][0]['HSR/SP'])
        metrics.append(data['metrics'][0]['rEXP'])
        metrics.append(data['metrics'][0]['rDIST'])
        metrics.append(data['metrics'][0]['rHSR'])
        metrics.append(data['metrics'][0]['rSPNT'])

        #create the labels array for the chart
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
                  "rHSR",
                  "rSPNT"]
        teamData = metrics

        #actual data to be passed to chart
        data = {
            "labels": labels,
            "default": teamData,
        }

        return Response(data)

#create the data to be passed to the chart on the team filter page
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
        athleteMetrics = []
        #run API calls to get all data regarding specific athlete
        teampro = teampro_queries.TeamProExample()
        team_id = teampro.get_team_id(team_name)
        player_id = teampro.get_player_id(team_name, firstName, lastName)
        metrics = teampro.get_individual_metrics_by_date(team_id, player_id, startDate, endDate)
        print(metrics)
        print(session)

        #loop through the JSON data and check if selected session is in the player's data
        convertData = json.dumps(metrics)
        data = json.loads(convertData)
        for item in data["metrics"]:
            print(item['Date'])
            populated = False
            #if date is found collect data
            if item['Date'] == session:
                print("FOUND:" + item['Date'])
                athleteMetrics.append((item["Duration"]))
                athleteMetrics.append((item["eTrimp"]))
                athleteMetrics.append((item["sTrimp"]))
                athleteMetrics.append((item["EXP"]))
                athleteMetrics.append((item["HR90"]))
                athleteMetrics.append((item["DIST"]))
                athleteMetrics.append((item["HSR"]))
                athleteMetrics.append((item["SPNT"]))
                athleteMetrics.append((item["HSR/SP"]))
                athleteMetrics.append((item["rEXP"]))
                athleteMetrics.append((item["rDIST"]))
                athleteMetrics.append((item["rHSR"]))
                athleteMetrics.append((item["rSPNT"]))
                populated = True

            if populated == True:
                break

        print(athleteMetrics)
        #generate labels for chart
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
        teamData = athleteMetrics
        # actual data to be passed to chart
        data = {
            "labels": labels,
            "default": teamData,
        }
        return Response(data)

#create the data to be passed to the chart on the home page
class HomeData(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):

        metrics = []
        data = HomeMetrics.get(self, request)

        print(data)

        #append each specific metric to the array for the chart data
        metrics.append(data['metrics'][0]['Duration'])
        metrics.append(data['metrics'][0]['eTrimp'])
        metrics.append(data['metrics'][0]['sTrimp'])
        metrics.append(data['metrics'][0]['EXP'])
        metrics.append(data['metrics'][0]['HR90'])
        metrics.append(data['metrics'][0]['DIST'])
        metrics.append(data['metrics'][0]['HSR'])
        metrics.append(data['metrics'][0]['SPNT'])
        metrics.append(data['metrics'][0]['HSR/SP'])
        metrics.append(data['metrics'][0]['rEXP'])
        metrics.append(data['metrics'][0]['rDIST'])
        metrics.append(data['metrics'][0]['rHSR'])
        metrics.append(data['metrics'][0]['rSPNT'])

        # generate labels for chart
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
        teamData = metrics
        # actual data to be passed to chart
        data = {
            "labels": labels,
            "default": teamData,
        }
        return Response(data)

#get data from API to populate the team dropdown
class Dropdown(APIView):

    def get(self, request, format=None):
        teampro_queries.TeamProExample.__init__(self)
        dropData = teampro_queries.TeamProExample.get_teams(self)

        return Response(dropData)

#get the team details containing player info for the athlete dropdown
class TeamDetails(APIView):

    def get(self, request, format=None):
        teampro = teampro_queries.TeamProExample()
        teamDetails = teampro.get_team_details(team_name)

        return Response(teamDetails)

#get the list of sessions for the team filter page
class TeamSessionDate(APIView):

    def get(self, request, format=None):

        strEndDate = str(endDate)
        strStartDate = str(startDate)

        teampro = teampro_queries.TeamProExample()
        teamSessions = teampro.get_session_dates_from_timeframe(team_name, strStartDate, strEndDate)
        return Response(teamSessions)

#get the team metrics for the team filter page
class TeamMetrics(APIView):

    def get(self,request, format=None):
        teampro = teampro_queries.TeamProExample()
        teamID = teampro.get_team_id(team_name)
        strEndDate = str(endDate)
        strStartDate = str(startDate)
        teamMetrics = teampro.get_team_metrics_by_date(teamID, strStartDate, strEndDate)

        return Response(teamMetrics)

#get data for summary page from API and summarize then pass that data to chart
class SumMetrics(APIView):

    def get(self, request, format=None):
        #get required data from API
        teampro = teampro_queries.TeamProExample()
        teamID = teampro.get_team_id(team_name)
        print(teamID)
        strEndDate = str(endDate)
        strStartDate = str(startDate)
        summaryMetrics = teampro.get_team_metrics_by_date(teamID, strStartDate, strEndDate)
        #get the summary of the data returned by the API
        sum = teampro.summarize_by_day(summaryMetrics)

        metrics = []
        data = sum

        print(data)
        #append each specific metric to the array for the chart data
        metrics.append(data['metrics'][0]['Duration'])
        metrics.append(data['metrics'][0]['eTrimp'])
        metrics.append(data['metrics'][0]['sTrimp'])
        metrics.append(data['metrics'][0]['EXP'])
        metrics.append(data['metrics'][0]['HR90'])
        metrics.append(data['metrics'][0]['DIST'])
        metrics.append(data['metrics'][0]['HSR'])
        metrics.append(data['metrics'][0]['SPNT'])
        metrics.append(data['metrics'][0]['HSR/SP'])
        metrics.append(data['metrics'][0]['rEXP'])
        metrics.append(data['metrics'][0]['rDIST'])
        metrics.append(data['metrics'][0]['rHSR'])
        metrics.append(data['metrics'][0]['rSPNT'])

        # generate labels for chart
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
                  "rHSR",
                  "rSPNT"]
        teamData = metrics
        # actual data to be passed to chart
        data = {
            "labels": labels,
            "default": teamData,
        }

        return Response(data)

