#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Request number of subreddit from API"""

    user_agent = '0x16-api_advanced-samedutm'
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)

    hdrs = {'User-Agent': user_agent}

    r = requests.get(url, headers=hdrs, allow_redirects=False)

    if r.status_code == 404:
        return 0

    res = r.json().get('data')
    return res.get('subscribers')
