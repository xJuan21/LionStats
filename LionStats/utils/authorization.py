#!/usr/bin/env python
from __future__ import print_function

import requests
from flask import Flask, request, redirect

from utils import load_config, save_config
from teampro import TeamPro


CALLBACK_PORT = 8000
CALLBACK_ENDPOINT = "/dashboard"

CONFIG_FILENAME = "config.yml"

REDIRECT_URL = "http://localhost:{}{}".format(CALLBACK_PORT, CALLBACK_ENDPOINT)

config = load_config(CONFIG_FILENAME)

teampro = TeamPro(client_id=config['client_id'],
                  client_secret=config['client_secret'],
                  redirect_url=REDIRECT_URL)


app = Flask(__name__)


@app.route("/")
def authorize():
    return redirect(teampro.authorization_url)


@app.route(CALLBACK_ENDPOINT)
def callback():
    """Callback for OAuth2 authorization request

    Saves the user's id and access token to a file.
    """

    #
    # Get authorization from the callback request parameters
    #
    authorization_code = request.args.get("code")

    #
    # Get an access token for the user using the authorization code.
    #
    # The authorization code is only valid for 10 minutes, so the access token
    # should be fetched immediately after the authorization step.
    #
    token_response = teampro.get_access_token(authorization_code)

    #
    # Save the user's id and access token to the configuration file.
    #
    # config["user_id"] = token_response["x_user_id"]
    config["access_token"] = token_response["access_token"]
    save_config(config, CONFIG_FILENAME)

    shutdown()
    return "Client authorized! You can now close this page."


def shutdown():
    shutdown_func = request.environ.get('werkzeug.server.shutdown')
    if shutdown_func is not None:
        shutdown_func()


def main():
    print("Navigate to http://localhost:{port}/ for authorization.\n".format(port=CALLBACK_PORT))
    app.run(host='localhost', port=CALLBACK_PORT)


if __name__ == "__main__":
    main()

