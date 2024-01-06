#!/usr/bin/python3
"""
Implements a script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


def json_api(url, query):
    """
    Sends a POST request to a URL with a letter as a parameter

    :param url: The url
    :param query: The letter to search
    :return: None
    """
    data = dict(q=query)
    r = requests.post(url, data)
    try:
        json_response = r.json()
        if len(json_response) == 0:
            print('No result')
        else:
            print('[{id}] {name}'.format(**json_response))
    except ValueError:
        print('Not a valid JSON')


if __name__ == '__main__':
    url_string = "http://0.0.0.0:5000/search_user"
    query_string = ""
    if len(sys.argv) > 1:
        query_string = sys.argv[1]

    json_api(url_string, query_string)
