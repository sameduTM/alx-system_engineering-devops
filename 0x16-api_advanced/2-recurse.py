#!/usr/bin/python3
"""Task 2 Module"""
import requests


def recurse(subreddit, hot_list=[], ct=0, aft=None):
    """ecursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit"""
    info_sub = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": ct, "after": aft},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if info_sub.status_code >= 400:
        return None

    var_hot_list = hot_list + [cld.get("data").get("title")
                               for cld in info_sub.json().get("data")
                               .get("children")]
    inf = info_sub.json()
    if not inf.get("data").get("after"):
        return var_hot_list

    return recurse(subreddit, var_hot_list, inf.get("data").get("countt"),
                   inf.get("data").get("after"))
