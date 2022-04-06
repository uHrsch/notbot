from datetime import datetime
import json
import pip._vendor.requests as requests


with open("./notbot/config.json") as config_file:
    config = json.load(config_file)


def get_twitch_headers():
    headers = {
        "Authorization": "Bearer {}".format(config["twitch_token"]),
        "Client-Id": config["twitch_id"]
    }
    
    return headers

 

def get_twitch_access_token():
    params = {
        "client_id": config["twitch_id"],
        "client_secret": config["twitch_secret"],
        "grant_type": "client_credentials"
    }

    response = requests.post("https://id.twitch.tv/oauth2/token", params=params)
    access_token = response.json()["access_token"]
    return access_token


def get_users(login_names):
    params = {
        "login": login_names
    }


    response = requests.get("https://api.twitch.tv/helix/users", params=params, headers=get_twitch_headers())
    return {entry["login"]: entry["id"] for entry in response.json()["data"]}


def get_streams(users):
    params = {
        "user_id": users.values()
    }
    response = requests.get("https://api.twitch.tv/helix/streams", params=params, headers=get_twitch_headers())

    return {entry["user_login"]: entry for entry in response.json()["data"]}


online_users = {}

def get_notifications():
    users = get_users(config["watchList"])
    streams = get_streams(users)

    notifications = []
    for user_name in config["watchList"]:
        if user_name not in online_users:
            online_users[user_name]  = datetime.utcnow()
        if user_name not in streams:
            online_users[user_name] = None
        else:
            started_at = datetime.strptime(streams[user_name]["started_at"], "%Y-%m-%dT%H:%M:%SZ")
            if online_users[user_name] is None or started_at > online_users[user_name]:
                notifications.append(streams[user_name])
                online_users[user_name] = started_at

    return notifications


get_notifications()