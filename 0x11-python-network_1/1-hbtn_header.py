#!/usr/bin/python3
"""
Implements a script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the header
of the response.
"""
import urllib.request
import sys


def send_request(url):
    """
    Displays the value of the X-Request-Id variable found in the header
    of the response.

    Args:
        url (string): The url to fetch
    """
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))


if __name__ == '__main__':
    send_request(sys.argv[1])
