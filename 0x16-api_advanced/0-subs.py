#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and returns the number of
    subscribers"""
    info_sub = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if info_sub.status_code >= 300:
        return 0

    return info_sub.json().get("data").get("subscribers")
