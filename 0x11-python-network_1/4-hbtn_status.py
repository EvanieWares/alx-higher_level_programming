#!/usr/bin/python3
"""
Implements a script that fetches https://alx-intranet.hbtn.io/status.
"""
import requests


def fetch_url(url):
    """
    Fetches a URL

    Args:
        url (string): The url to fetch
    """
    r = requests.get(url)
    body = r.text
    print('Body response:')
    print(f'\t- type: {type(body)}')
    print(f'\t- content: {body}')


if __name__ == '__main__':
    url_string = "https://alx-intranet.hbtn.io/status"
    fetch_url(url_string)
