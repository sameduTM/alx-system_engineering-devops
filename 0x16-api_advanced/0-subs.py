#!/usr/bin/python3
"""0. How many subs?"""
import requests
import requests.auth


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    client_auth = requests.auth.HTTPBasicAuth(
        'IGV5ZuvVzBLOPag9Z6JCsQ', 'iuLrVl0bzohNU9XLoTO_eygaRg3pZA')
    post_data = {"grant_type": "password",
                 "username": "Rough_Drink_171", "password": "@Yeah_Yebaba884"}
    headers = {"User-Agent": "ChangeMeClient/0.1 by Rough_Drink_171"}
    response = requests.post("https://www.reddit.com/api/v1/access_token",
                             auth=client_auth, data=post_data, headers=headers)

    token = response.json()['access_token']

    headers = {"Authorization": "bearer {}".format(
        token), "User-Agent": "ChangeMeClient/0.1 by Rough_Drink_171"}

    response = requests.get(
        "https://oauth.reddit.com/r/{}/about".format(subreddit),
        headers=headers, allow_redirects=False)
    try:
        x = response.json()['data']['subscribers']
        return x
    except Exception:
        return 0
