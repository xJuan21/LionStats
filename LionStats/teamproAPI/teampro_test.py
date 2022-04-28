from __future__ import print_function
import sys

sys.path.append('C:/LionStats/LionStats/teamproAPI')
sys.path.append('/Users/connor/PycharmProjects/LionStats2.0/LionStats/teamproAPI')

from APIutils import load_config, pretty_print_json

import requests
import json
import yaml
CONFIG_FILENAME = "config.yml"

class TeamProExample(object):

    def __init__(self):
        self.config = load_config(CONFIG_FILENAME)
        # self.get_team_details("Women's Lacrosse")

    #get json data
    ##################################
    def get_teams(self):
        headers = {
          'Accept': 'application/json',
          'Authorization': 'Bearer {}'.format(self.config["access_token"])
        }

        teams = requests.get('https://teampro.api.polar.com/v1/teams', params={}, headers=headers)
        #pretty_print_json(teams.json())
        return teams.json()

    def get_team_id(self, team_name):
        teams_data = self.get_teams()
        team_id = ''

        for keyval in teams_data['data']:
            if team_name == keyval['name']:
                team_id = keyval['id']

        return team_id

    def get_team_details(self, team_name):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer {}'.format(self.config["access_token"])
        }

        team_id = self.get_team_id(team_name)

        team_details = requests.get('https://teampro.api.polar.com/v1/teams/{}'.format(team_id),
                                    params={}, headers=headers)

        # pretty_print_json(team_details.json())
        return team_details.json()

    def get_team_training_sessions(self, team_name):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer {}'.format(self.config["access_token"])
        }

        team_id = self.get_team_id(team_name)

        team_training_sessions = requests.get('https://teampro.api.polar.com/v1/teams/{}/training_sessions'
                                              .format(team_id), params={}, headers=headers)

        # pretty_print_json(team_training_sessions.json())
        return team_training_sessions.json()
    ##################################

    # queries
    def get_teams_list(self):
        teams_data = self.get_teams()
        teams_list = []

        for keyval in teams_data['data']:
            teams_list.append(keyval['name'])

        print(teams_list)
        return teams_list


if __name__ == "__main__":
    TeamProExample()
