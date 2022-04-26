from __future__ import print_function

from utils import load_config, pretty_print_json

import requests
import json
import isodate
import datetime

CONFIG_FILENAME = "config.yml"

# MAKE SURE TO AUTHORIZE BEFORE USING THIS CLASS BY RUNNING 'python authorization.py'!!!
# YOU WILL GET AN ERROR IF YOU DON'T!

class TeamProExample(object):

    def __init__(self):
        self.config = load_config(CONFIG_FILENAME)

        # hardcoded ids for examples; uncomment to test functions
        # note: these aren't very efficient
        team_id = self.get_team_id("Women's Lacrosse")
        #training_session_id = self.get_training_session_id(team_id, "2022-01-10")
        #player_id = self.get_player_id(team_id, "Meg", "Rea")
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
        #players = self.get_players(team_id)
        #print(self.get_player_names(players))
        metrics_by_date = self.get_team_metrics_by_date(team_id, "03/20/2022", "04/03/2022")
        #pretty_print_json(metrics_by_date)
        pretty_print_json(self.summarize_by_month(metrics_by_date))

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

        team_training_sessions = \
            requests.get('https://teampro.api.polar.com/v1/teams/{}/training_sessions?page=0&per_page=100'
                         .format(team_id), params={}, headers=headers)
        str_sessions = team_training_sessions.json()

        sessions = {"data": []}
        for keyval in str_sessions['data']:
            sessions["data"].append(keyval)

        total_pages = str_sessions['page']['total_pages']

        for i in range(total_pages-1):
            team_training_sessions = \
                requests.get('https://teampro.api.polar.com/v1/teams/{}/training_sessions?page={}&per_page=100'
                             .format(team_id, i), params={}, headers=headers)
            str_sessions = team_training_sessions.json()

            for keyval in str_sessions['data']:
                sessions["data"].append(keyval)

        return sessions

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

        str_sessions = player_training_sessions.json()

        sessions = {"data": []}
        for keyval in str_sessions['data']:
            sessions["data"].append(keyval)

        total_pages = str_sessions['page']['total_pages']

        for i in range(total_pages - 1):
            player_training_sessions = \
                requests.get('https://teampro.api.polar.com/v1/teams/{}/training_sessions?page={}&per_page=100'
                             .format(player_id, i), params={}, headers=headers)
            str_sessions = player_training_sessions.json()

            for keyval in str_sessions['data']:
                sessions["data"].append(keyval)

        return sessions

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

    # returns a json string of players on a specific team given a team_id
    def get_players(self, team_id):
        team_details = self.get_team_details(team_id)
        players = {"players": []}

        for keyval in team_details['data']['players']:
            players["players"].append(keyval)

        return players

    # returns a list of player names given a json string of players (call get_players method first)
    def get_player_names(self, players):
        players_list = []

        for keyval in players['players']:
            players_list.append(keyval['first_name'] + " " + keyval['last_name'])

        return players_list

    # within a specified time frame, return a json string of the calculated metrics for every player team session
    # this can take a while to run... it seems to take about a second to make one get request from the API, and this
    # begins to add up very quickly since we will be accessing many player sessions at once
    def get_team_metrics_by_date(self, team_id, start_date, end_date):
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
        player_ids = []
        for item in (session_ids):
            team_training_session_details = self.get_team_training_session_details(item)['data']

            for keyval in team_training_session_details['participants']:
                player_session_ids.append(keyval['player_session_id'])
                player_ids.append(keyval['player_id'])

        # append all calculated metrics from every player and session during specified time frame to a json string
        all_metrics = {"metrics": []}
        for i, item in enumerate(player_session_ids):
            summary = self.get_player_team_training_session_summary(item)['data']
            metrics = self.calculate_metrics(summary, summary['created'][0:10], player_ids[i])
            all_metrics["metrics"].append(metrics)

        return all_metrics

    # given a player team training session summary, a date, and a player ID, calculate metrics needed for
    # dashboard and return a json string with the date as well as those metrics
    def calculate_metrics(self, summary, start_date, player_id):
        player = player_id
        date = start_date

        # heart rate zones
        hr_zones = []
        for keyval in summary['heart_rate_zones']:
            hr_zones.append(datetime.timedelta.total_seconds(isodate.parse_duration(keyval['in_zone'])) / 60)

        # speed zones
        speed_zones = []
        for keyval in summary['speed_zones_kmh']:
            speed_zones.append(keyval['in_zone_meters'])

        # acceleration zones
        accel_zones = []
        for keyval in summary['acceleration_zones_ms2']:
            accel_zones.append(keyval['count'])

        # calculations
        duration = int(summary['duration_ms'])/60000
        e_trimp = (hr_zones[0] * 1) + (hr_zones[1] * 2) + ((hr_zones[2]) * 3) + (hr_zones[3] * 4) + (hr_zones[4] * 5)
        s_trimp = ((speed_zones[0] * 1) + (speed_zones[1] * 2) + ((speed_zones[2]) * 3) + (speed_zones[3] * 4)
                   + (speed_zones[4] * 5))/100
        exp = accel_zones[0] + accel_zones[1] + accel_zones[-2] + accel_zones[-1]
        hr90 = hr_zones[4]
        dist = summary['distance_meters']
        hsr = speed_zones[-2] + speed_zones[-1]
        spnt = speed_zones[-1]
        hsr_div_sp = 0
        if summary['sprint_counter'] != 0:
            hsr_div_sp = hsr/summary['sprint_counter']
        r_exp = exp/duration
        r_dist = dist/duration
        r_hsr = hsr/duration
        r_spnt = spnt/duration

        # create the objects to be appended
        player_id_obj = {"player_id": player}
        date_obj = {"Date": date}
        duration_obj = {"Duration": duration}
        e_trimp_obj = {"eTrimp": e_trimp}
        s_trimp_obj = {"sTrimp": s_trimp}
        exp_obj = {"EXP": exp}
        hr90_obj = {"HR90": hr90}
        dist_obj = {"DIST": dist}
        hsr_obj = {"HSR": hsr}
        spnt_obj = {"SPNT": spnt}
        hsr_div_sp_obj = {"HSR/SP": hsr_div_sp}
        r_exp_obj = {"rEXP": r_exp}
        r_dist_obj = {"rDIST": r_dist}
        r_hsr_obj = {"rHSR": r_hsr}
        r_spnt_obj = {"rSPNT": r_spnt}

        # append objects into json string
        json_metrics = '{}'
        json_str = json.loads(json_metrics)

        json_str.update(player_id_obj)
        json_str.update(date_obj)
        json_str.update(duration_obj)
        json_str.update(e_trimp_obj)
        json_str.update(s_trimp_obj)
        json_str.update(exp_obj)
        json_str.update(hr90_obj)
        json_str.update(dist_obj)
        json_str.update(hsr_obj)
        json_str.update(spnt_obj)
        json_str.update(hsr_div_sp_obj)
        json_str.update(r_exp_obj)
        json_str.update(r_dist_obj)
        json_str.update(r_hsr_obj)
        json_str.update(r_spnt_obj)

        return json_str

    # given a list of metrics (most likely from get_team_metrics_by_date() method), return team averages by month for
    # each metric
    def summarize_by_month(self, metrics):
        months = []
        count = 0
        months_json = '{}'
        months_json = json.loads(months_json)

        # metrics sums
        duration_sum = 0
        e_trimp_sum = 0
        s_trimp_sum = 0
        exp_sum = 0
        hr90_sum = 0
        dist_sum = 0
        hsr_sum = 0
        spnt_sum = 0
        hsr_div_sp_sum = 0
        r_exp_sum = 0
        r_dist_sum = 0
        r_hsr_sum = 0
        r_spnt_sum = 0

        # metrics averages
        duration_avg = 0
        e_trimp_avg = 0
        s_trimp_avg = 0
        exp_avg = 0
        hr90_avg = 0
        dist_avg = 0
        hsr_avg = 0
        spnt_avg = 0
        hsr_div_sp_avg = 0
        r_exp_avg = 0
        r_dist_avg = 0
        r_hsr_avg = 0
        r_spnt_avg = 0

        for keyval in metrics['metrics']:
            curr_month = keyval['Date'][0:7]
            if curr_month not in months:
                if len(months) > 0:
                    month_to_add = {"{}".format(months[len(months) - 1]): []}

                    duration_obj = {"Duration": duration_avg}
                    e_trimp_obj = {"eTrimp": e_trimp_avg}
                    s_trimp_obj = {"sTrimp": s_trimp_avg}
                    exp_obj = {"EXP": exp_avg}
                    hr90_obj = {"HR90": hr90_avg}
                    dist_obj = {"DIST": dist_avg}
                    hsr_obj = {"HSR": hsr_avg}
                    spnt_obj = {"SPNT": spnt_avg}
                    hsr_div_sp_obj = {"HSR/SP": hsr_div_sp_avg}
                    r_exp_obj = {"rEXP": r_exp_avg}
                    r_dist_obj = {"rDIST": r_dist_avg}
                    r_hsr_obj = {"rHSR": r_hsr_avg}
                    r_spnt_obj = {"rSPNT": r_spnt_avg}

                    json_metrics = '{}'
                    json_str = json.loads(json_metrics)
                    json_str.update(duration_obj)
                    json_str.update(e_trimp_obj)
                    json_str.update(s_trimp_obj)
                    json_str.update(exp_obj)
                    json_str.update(hr90_obj)
                    json_str.update(dist_obj)
                    json_str.update(hsr_obj)
                    json_str.update(spnt_obj)
                    json_str.update(hsr_div_sp_obj)
                    json_str.update(r_exp_obj)
                    json_str.update(r_dist_obj)
                    json_str.update(r_hsr_obj)
                    json_str.update(r_spnt_obj)

                    month_to_add["{}".format(months[len(months) - 1])].append(json_str)
                    months_json.update(month_to_add)

                months.append(curr_month)
                duration_sum = keyval['Duration']
                e_trimp_sum = keyval['eTrimp']
                s_trimp_sum = keyval['sTrimp']
                exp_sum = keyval['EXP']
                hr90_sum = keyval['HR90']
                dist_sum = keyval['DIST']
                hsr_sum = keyval['HSR']
                spnt_sum = keyval['SPNT']
                hsr_div_sp_sum = keyval['HSR/SP']
                r_exp_sum = keyval['rEXP']
                r_dist_sum = keyval['rDIST']
                r_hsr_sum = keyval['rHSR']
                r_spnt_sum = keyval['rSPNT']
            else:
                count += 1

                duration_sum += keyval['Duration']
                e_trimp_sum += keyval['eTrimp']
                s_trimp_sum += keyval['sTrimp']
                exp_sum += keyval['EXP']
                hr90_sum += keyval['HR90']
                dist_sum += keyval['DIST']
                hsr_sum += keyval['HSR']
                spnt_sum += keyval['SPNT']
                hsr_div_sp_sum += keyval['HSR/SP']
                r_exp_sum += keyval['rEXP']
                r_dist_sum += keyval['rDIST']
                r_hsr_sum += keyval['rHSR']
                r_spnt_sum += keyval['rSPNT']

                duration_avg = duration_sum / count
                e_trimp_avg = e_trimp_sum / count
                s_trimp_avg = s_trimp_sum / count
                exp_avg = exp_sum / count
                hr90_avg = hr90_sum / count
                dist_avg = dist_sum / count
                hsr_avg = hsr_sum / count
                spnt_avg = spnt_sum / count
                hsr_div_sp_avg = hsr_div_sp_sum / count
                r_exp_avg = r_exp_sum / count
                r_dist_avg = r_dist_sum / count
                r_hsr_avg = r_hsr_sum / count
                r_spnt_avg = r_spnt_sum / count

        month_to_add = {"{}".format(months[len(months) - 1]): []}

        duration_obj = {"Duration": duration_avg}
        e_trimp_obj = {"eTrimp": e_trimp_avg}
        s_trimp_obj = {"sTrimp": s_trimp_avg}
        exp_obj = {"EXP": exp_avg}
        hr90_obj = {"HR90": hr90_avg}
        dist_obj = {"DIST": dist_avg}
        hsr_obj = {"HSR": hsr_avg}
        spnt_obj = {"SPNT": spnt_avg}
        hsr_div_sp_obj = {"HSR/SP": hsr_div_sp_avg}
        r_exp_obj = {"rEXP": r_exp_avg}
        r_dist_obj = {"rDIST": r_dist_avg}
        r_hsr_obj = {"rHSR": r_hsr_avg}
        r_spnt_obj = {"rSPNT": r_spnt_avg}

        json_metrics = '{}'
        json_str = json.loads(json_metrics)
        json_str.update(duration_obj)
        json_str.update(e_trimp_obj)
        json_str.update(s_trimp_obj)
        json_str.update(exp_obj)
        json_str.update(hr90_obj)
        json_str.update(dist_obj)
        json_str.update(hsr_obj)
        json_str.update(spnt_obj)
        json_str.update(hsr_div_sp_obj)
        json_str.update(r_exp_obj)
        json_str.update(r_dist_obj)
        json_str.update(r_hsr_obj)
        json_str.update(r_spnt_obj)

        month_to_add["{}".format(months[len(months) - 1])].append(json_str)
        months_json.update(month_to_add)

        return months_json

    # given a list of metrics (most likely from get_team_metrics_by_date() method), return team averages by week for
    # each metric (WORK IN PROGRESS)
    #def summarize_by_week(self, metrics):

    # given a list of metrics (most likely from get_team_metrics_by_date() method), return team averages by day for
    # each metric (WORK IN PROGRESS)
    #def summarize_by_day(self, metrics):

    ##################################


if __name__ == "__main__":
    TeamProExample()
