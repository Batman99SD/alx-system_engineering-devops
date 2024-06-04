#!/usr/bin/python3
'''
recursive
'''

import requests


def recurse(subreddit, hot_list=[], after=None):
    '''
    queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function should return None.
    queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function should return None.
    '''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "CustomUserAgent/0.1"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get('data')
        if not data:
            return None

        hot_list.extend([post['data']['title'] for post in data['children']])
        after = data.get('after')

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except requests.RequestException:
        return None
