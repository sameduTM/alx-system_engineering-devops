#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """get first 10 hot posts"""

    usr_agent = '0x16-api_advanced-samedutm'
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    hdrs = {'User-Agent': usr_agent}

    r = requests.get(url, headers=hdrs, allow_redirects=False)

    if r.status_code != 200:
        print('None')
    else:
        dta = r.json()['data']

        content = dta['children']
        for c in content:
            print(c['data']['title'])
