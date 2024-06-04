#!/usr/bin/python3
'''
Module to fetch top ten hot posts from a subreddit.

This module contains a function that fetches and prints the titles
of the top ten hot posts from a given subreddit using the Reddit API.
'''

import requests


def top_ten(subreddit):
    '''
    Fetch and print the titles of the top ten hot posts from a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Prints:
        The titles of the top ten hot posts, or None if the request fails.
    '''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "CustomUserAgent/0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)
