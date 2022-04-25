#!/usr/bin/env python

import json
import os.path

import yaml


def load_config(filename):
    """Load configuration from a yaml file"""
    BASE = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(BASE, "config.yml")) as f:
        return yaml.safe_load(f)


def save_config(config, filename):
    """Save configuration to a yaml file"""
    with open(filename, "w+") as f:
        yaml.safe_dump(config, f, default_flow_style=False)



def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))
