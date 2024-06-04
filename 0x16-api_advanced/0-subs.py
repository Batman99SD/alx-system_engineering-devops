#!/usr/bin/python3
'''
Number of subscribers
'''

import requests

def number_of_subscribers(subreddit):
    '''
    Gets the number of subscribers of a subreddit
    Args:
        subreddit (str): The name of the subreddit.

    Prints:
        The number of subscribers, or None if the request fails.
    '''
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "CustomUserAgent/0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
