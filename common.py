#!/usr/bin/env python

import configparser
import json
import os

import requests

config = configparser.ConfigParser()
config.read(os.path.expanduser("~/.avast.ini"))


apiurl = "https://asociacionavast.playoffinformatica.com/api.php/api/v1.0"
headers = {"Content-Type": "application/json", "content-encoding": "gzip"}


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


def gettoken(user=config["auth"]["username"], password=config["auth"]["password"]):

    apiurl = "https://asociacionavast.playoffinformatica.com/api.php/api/v1.0"

    # get token

    loginurl = apiurl + "/login/colegi"

    data = {"username": user, "password": password}

    result = requests.post(loginurl, data=json.dumps(data), headers=headers)

    token = result.json()["access_token"]

    return token


def writejson(filename, data):
    with open("data/%s.json" % filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        return True


def rewadjson(filename):
    with open("data/%s.json" % filename, "r", encoding="utf-8") as f:
        mydata = json.load(f)
        return mydata