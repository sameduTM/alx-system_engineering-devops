#!/usr/bin/python3
"""queries the Reddit API, parses the title of all hot articles, and prints a
sorted count of given keywords (case-insensitive, delimited by spaces"""


import requests


def count_words(subreddit, word_list, count_list=[], next_page=None):
    """recursive function"""
    if not count_list:
        for wrd in word_list:
            count_list.append(dict({'keyword': wrd, 'count': 0}))

    usr_agent = '0x16-api_advanced-samedutm'
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    if next_page:
        url += '?after={}'.format(next_page)

    hdrs = {'User-Agent': usr_agent}

    r = requests.get(url, headers=hdrs, allow_redirects=False)

    if r.status_code != 200:
        return

    dta = r.json()['data']

    texts = dta['children']
    for text in texts:
        title = text['data']['title']
        for item in count_list:
            title_lwr = title.lower()
            title_lst = title_lwr.split()
            item['count'] += title_lst.count(item['keyword'].lower())

    next_page = dta['after']
    if next_page:
        return count_words(subreddit, word_list, count_list, next_page)
    else:
        sort_list = sorted(count_list, key=lambda word: (
            word['count'], word['keyword']), reverse=True)
        keywrd_mtc = 0

        for wrd in sort_list:
            if wrd['count'] > 0:
                print('{}: {}'.format(wrd['keyword'], wrd['count']))
                keywrd_mtc += 1
        return
