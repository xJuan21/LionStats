#!/usr/bin/env python

import json
import os.path

import yaml


def load_config(filename):
    """Load configuration from a yaml file"""
    #BASE = os.path.dirname(os.path.abspath(__file__))
    BASE = "C:\LionStats\LionStats/teamproAPI"
    #BASE = "C:/LionStats/dist/manage/teamproAPI"
    print(BASE)
    with open(os.path.join(BASE, "config.yml")) as f:
        return yaml.safe_load(f)


def save_config(config, filename):
    """Save configuration to a yaml file"""
    #"C:/LionStats/dist/manage/teamproAPI/config.yml"
    with open("C:/LionStats/LionStats/teamproAPI/config.yml", "w+") as f:
        yaml.safe_dump(config, f, default_flow_style=False)



def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))