#!/usr/bin/python3
"""Task 1 module"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit."""
    info_sub = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if info_sub.status_code >= 300:
        print("None")
    else:
        [print(cld.get("data").get("title"))
         for cld in info_sub.json().get("data").get("children")]
