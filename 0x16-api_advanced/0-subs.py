#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Request number of subreddit from API"""

    usr_agent = '0x16-api_advanced-samedutm'
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)

    hdrs = {'User-Agent': usr_agent}

    r = requests.get(url, headers=hdrs, allow_redirects=False)

    if r.status_code != 200:
        return 0

    dta = r.json()['data']

    pgs = dta['children']

    pg_dta = pgs[0]['data']

    return pg_dta['subreddit_subscribers']
