#!/usr/bin/python3
"""
Implements a script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
import urllib.error
import urllib.request
import sys


def error_code(url):
    """
    Displays the body of the response

    Args:
        url (string): The url to fetch
    """
    try:
        with urllib.request.urlopen(url) as resp:
            body = resp.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')


if __name__ == '__main__':
    error_code(sys.argv[1])
