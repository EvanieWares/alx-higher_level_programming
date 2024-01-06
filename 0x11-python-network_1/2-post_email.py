#!/usr/bin/python3
"""
Implements a script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
from urllib import request, parse
import sys


def post_email(url, email):
    """
    Sends a POST request to a URL and displays the body of the response

    Args:
        url (string): The url to fetch
        email (string): The email to post
    """
    values = {'email': email}
    data = parse.urlencode(values).encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as resp:
        body = resp.read().decode('utf-8')
        print(body)


if __name__ == '__main__':
    url_string, email_string = sys.argv[1:3]
    post_email(url_string, email_string)
