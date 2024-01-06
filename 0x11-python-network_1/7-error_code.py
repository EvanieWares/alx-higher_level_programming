#!/usr/bin/python3
"""
Implements a script that takes in a URL, sends a request to the URL and
displays the body of the response.
"""
import requests
import sys


def error_code(url):
    """
    Displays the body of the response

    Args:
        url (string): The url to fetch
    """
    r = requests.get(url)
    if r.status_code >= 400:
        print(f'Error code: {r.status_code}')
    else:
        print(r.text)


if __name__ == '__main__':
    error_code(sys.argv[1])
