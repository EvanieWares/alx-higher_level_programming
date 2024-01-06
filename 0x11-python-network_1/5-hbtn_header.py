#!/usr/bin/python3
"""
Implements a script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header.
"""
import requests
import sys


def send_request(url):
    """
    Displays the value of the X-Request-Id variable found in the
    response header.

    Args:
        url (string): The url to fetch
    """
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))


if __name__ == '__main__':
    send_request(sys.argv[1])
