This module defines the function `number_of_subscribers`
which queries the Reddit API to get the number of subscribers
for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for the given subreddit. If the subreddit is invalid, returns 0.
    """
    # Set up the headers with a custom User-Agent
    headers = {'User-Agent': 'MyRedditScript/0.1'}

    # Make a GET request to the Reddit API
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is valid
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
