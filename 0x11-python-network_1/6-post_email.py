#!/usr/bin/python3
"""
Implements a script that takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter, and finally
displays the body of the response
"""
import requests
import sys


def post_email(url, email):
    """
    Sends a POST request to a URL and displays the body of the response

    Args:
        url (string): The url to fetch
        email (string): The email to post
    """
    # print(help(requests))
    data = dict(email=email)
    r = requests.post(url, data)
    print(r.text)


if __name__ == '__main__':
    url_string, email_string = sys.argv[1:3]
    post_email(url_string, email_string)
