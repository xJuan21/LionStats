from __future__ import print_function

from utils import load_config, pretty_print_json

import requests
import json

CONFIG_FILENAME = "config.yml"

# MAKE SURE TO AUTHORIZE BEFORE USING THIS CLASS BY RUNNING 'python authorization.py'!!!
# YOU WILL GET AN ERROR IF YOU DON'T!

class TeamProExample(object):

    def __init__(self):
        self.config = load_config(CONFIG_FILENAME)

        # hardcoded ids for examples; uncomment to test functions
        # note: these aren't very efficient
        team_id = self.get_team_id("Women's Lacrosse")
        #training_session_id = self.get_training_session_id(team_id, "2022-04-03")
        #player_id = self.get_player_id(team_id, "Alyssa", "Kneedler")
        #player_session_id = self.get_player_session_id(training_session_id, player_id)

        # test runs of each function that returns .json data
        #pretty_print_json(self.get_teams())
        #pretty_print_json(self.get_team_details(team_id))
        #pretty_print_json(self.get_team_training_sessions(team_id))
        #pretty_print_json(self.get_team_training_session_details(training_session_id))
        #pretty_print_json(self.get_player_training_sessions(player_id))
        #pretty_print_json(self.get_player_training_session_details(player_session_id))
        #pretty_print_json(self.get_player_team_training_session_summary(player_session_id))

        # queries tests
        #print(self.get_teams_list())
        pretty_print_json(self.get_metrics_by_date(team_id, "03/29/2021", "04/03/2022"))

    # functions that return .json data
    # vist https://www.polar.com/teampro-api/#teampro-api for example responses
    ##################################
    # description: list of all LU teams using Polar devices
    # 'data' attributes for each team: id, name, organization, created, modified
    # 'page': per_page, total_elements, page_number, total_pages
    def get_teams(self):
        headers = {
          'Accept': 'application/json',
          'Authorization': 'Bearer {}'.format(self.config["access_token"])
        }

        teams = requests.get('https://teampro.api.polar.com/v1/teams', params={}, headers=headers)
        return teams.json()

    # description: details of a specific team, given the team_id
    # 'data': id, name, organization, created, modified, players
    # 'players' list attributes: player_id, player_number, role, first_name, last_name
    def get_team_details(self, team_id):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer {}'.format(self.config["access_token"])
        }

        team_details = requests.get('https://teampro.api.polar.com/v1/teams/{}'.format(team_id),
                                    params={}, headers=headers)

        return team_details.json()

    # description: list of all training sessions for a specific team, given the team_id
    # 'data' attributes for each session: id, team_id, name, type, note, created, modified, record_start_time,
    #                                     start_time, end_time, latitude, longitude, sport
    # 'page': per_page, total_elements, page_number, total_pages
    def get_team_training_sessions(self, team_id):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer {}'.format(self.config["access_token"])
        }

        team_training_sessions = requests.get('https://teampro.api.polar.com/v1/teams/{}/training_sessions'
                                              .format(team_id), params={}, headers=headers)

        return team_training_sessions.json()

    # description: details of a training session, given the training_session_id
    # 'data': id, team_id, name, type, note, created, modified, record_start_time,
    #         start_time, end_time, latitude, longitude, sport, arena, participants, markers
    # 'participants' list attributes: player_id, player_number, role, player_session_id
    # 'markers' list attributes: start_time, end_time, marker_type, name, note
    def get_team_training_session_details(self, training_session_id):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer {}'.format(self.config["access_token"])
        }

        session_details = requests.get('https://teampro.api.polar.com/v1/teams/training_sessions/{}'
                                       .format(training_session_id), params={}, headers=headers)

        return session_details.json()

    # description: list of all player training sessions for a specific player, given the player_id
    # 'data' attributes for each session: id, type, created, modified, sport, name, feeling, note, latitude,
    #                                     longitude, start_time, stop_time, duration_ms, timezone_offset
    # 'page': per_page, total_elements, page_number, total_pages
    def get_player_training_sessions(self, player_id):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer {}'.format(self.config["access_token"])
        }

        player_training_sessions = requests.get('https://teampro.api.polar.com/v1/players/{}/training_sessions'
                                                .format(player_id), params={}, headers=headers)

        return player_training_sessions.json()

    # description: details of a player's training session, given the player_session_id
    # 'data': id, type, created, modified, name, feeling, note, latitude, longitude, start_time, stop_time, duration_ms,
    #         calories, distance_meters, training_load, recovery_time_ms, fat_percentage, heart_rate_max,
    #         hear_rate_avg, sport, running_index, ascent, descent, sprint_counter, product, samples, rr_intervals
    # 'samples': fields, values
    def get_player_training_session_details(self, player_session_id):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer {}'.format(self.config["access_token"])
        }

        session_details = requests.get('https://teampro.api.polar.com/v1/training_sessions/{}'
                                       .format(player_session_id), params={}, headers=headers)

        return session_details.json()

    # description: get trimmed values for a player's team training session
    # 'data': player_session_id, created, modified, trimmed_start_time, duration_ms, distance_meters, kilo_calories,
    #         heart_rate_max, heart_rate_avg, heart_rate_min, heart_rate_max_percent, heart_rate_avg_percent,
    #         heart_rate_min_percent, sprint_counter, speed_avg_kmh, speed_max_kmh, cadence_avg, cadence_max,
    #         training_load, heart_rate_zones, speed_zones_kmh, acceleration_zones_ms2
    # 'heart_rate_zones' list attributes: index, lower-limit, upper-limit, in-zone
    # 'speed_zones_kmh' list attributes: index, lower-limit, upper-limit, in-zone_meters
    # 'acceleration_zones_ms2' list attributes: limit, counter
    def get_player_team_training_session_summary(self, player_session_id):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer {}'.format(self.config["access_token"])
        }

        session_summary = requests.get('https://teampro.api.polar.com/v1/training_sessions/{}/session_summary'
                                       .format(player_session_id), params={}, headers=headers)

        return session_summary.json()
    ##################################

    # *get team_id, training_session_id, player_id, and player_session_id
    # *used for testing
    # *may need to be modified or might not be used at all depending on how we want
    #   to access ids and what .json data we have access to at the time
    ##################################
    # use team_name to get team_id; case-sensitive
    def get_team_id(self, team_name):
        teams_data = self.get_teams()
        team_id = ''

        for keyval in teams_data['data']:
            if team_name == keyval['name']:
                team_id = keyval['id']

        return team_id

    # use team_id and date to get session_id for particular session
    # date format: year-month-day (####-##-##)
    def get_training_session_id(self, team_id, date):
        team_training_sessions = self.get_team_training_sessions(team_id)
        session_id = ''

        for keyval in team_training_sessions['data']:
            if date == keyval['start_time'][0:10]:
                session_id = keyval['id']

        return session_id

    # use team_id, and player first_name and last_name to get player_id; case-sensitive
    def get_player_id(self, team_id, first_name, last_name):
        team_details = self.get_team_details(team_id)
        player_id = ''

        for keyval in team_details['data']['players']:
            if first_name == keyval['first_name'] and last_name == keyval['last_name']:
                player_id = keyval['player_id']

        return player_id

    # use player_id and training_session_id to get player_session_id for particular session
    def get_player_session_id(self, training_session_id, player_id):
        team_training_session_details = self.get_team_training_session_details(training_session_id)
        player_session_id = ''

        for keyval in team_training_session_details['data']['participants']:
            if player_id == keyval['player_id']:
                player_session_id = keyval['player_session_id']

        return player_session_id
    ##################################

    # queries
    ##################################
    # returns a list of strings containing the names of all existing teams
    def get_teams_list(self):
        teams_data = self.get_teams()
        teams_list = []

        for keyval in teams_data['data']:
            teams_list.append(keyval['name'])

        return teams_list

    # WORK IN PROGRESS!!!
    # within a specified time frame, return a json string of the calculated metrics for every player team session
    # this can take a while to run... it seems to take about a second to make one get request from the API, and this
    # begins to add up very quickly since we will be accessing many player sessions at once
    def get_metrics_by_date(self, team_id, start_date, end_date):
        # get all training sessions for a specific team
        training_sessions = self.get_team_training_sessions(team_id)

        # format start and end dates for easy access from API
        formatted_start_date = start_date[6:10] + "-" + start_date[0:2] + "-" + start_date[3:5]
        formatted_end_date = end_date[6:10] + "-" + end_date[0:2] + "-" + end_date[3:5]

        # get all session ids that exist within specified time frame
        session_ids = []
        for keyval in training_sessions['data']:
            if formatted_start_date <= keyval['start_time'][0:10] <= formatted_end_date:
                session_ids.append(keyval['id'])

        # get all player session ids from every session that exists within specified time frame
        player_session_ids = []
        for item in session_ids:
            team_training_session_details = self.get_team_training_session_details(item)['data']

            for keyval in team_training_session_details['participants']:
                player_session_ids.append(keyval['player_session_id'])

        # append all calculated metrics from every player and session during specified time frame to a json string
        all_metrics = {"Metrics": []}
        for item in player_session_ids:
            summary = self.get_player_team_training_session_summary(item)['data']
            metrics = self.calculate_metrics(summary, summary['created'][0:10])
            all_metrics["Metrics"].append(metrics)

        return all_metrics

    # WORK IN PROGRESS!!!
    # given a player team training session summary, as well as the date for that session, calculate metrics needed for
    # dashboard and return a json string with the date as well as those metrics
    def calculate_metrics(self, summary, start_date):
        # calculations
        date = start_date
        duration = int(summary['duration_ms'])/6000
        e_trimp = ''
        s_trimp = ''
        exp = ''
        hr90 = ''
        dist = ''
        hsr = ''
        spnt = ''
        hsr_div_sp = ''
        r_exp = ''
        r_dist = ''
        r_hsr = ''
        r_spnt = ''

        # create the objects to be appended
        date_obj = {"Date": date}
        duration_obj = {"Duration": duration}

        # append objects into json string
        json_metrics = '{}'
        json_str = json.loads(json_metrics)

        json_str.update(date_obj)
        json_str.update(duration_obj)

        return json_str
    ##################################


if __name__ == "__main__":
    TeamProExample()
