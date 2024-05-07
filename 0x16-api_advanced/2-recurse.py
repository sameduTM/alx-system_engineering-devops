#!/usr/bin/python3
"""Query API to get sub count"""

import requests


def recurse(subreddit, hot_list=[], next_page=None, count=0):
    """ecursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit"""
    usr_agent = '0x16-api_advanced-samedutm'
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    if next_page:
        url += '?after={}'.format(next_page)

    hdrs = {'User-agent': usr_agent}
    r = requests.get(url, headers=hdrs, allow_redirects=False)

    if r.status_code != 200:
        return None

    dta = r.json()['data']

    texts = dta['children']

    for txt in texts:
        count += 1
        hot_list.append(txt['data']['title'])

    next_page = dta['after']
    if next_page is not None:
        return recurse(subreddit, hot_list, next_page, count)
    else:
        return hot_list
