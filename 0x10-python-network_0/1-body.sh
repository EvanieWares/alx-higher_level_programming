#!/bin/bash
# This script sends a GET request to a given URL and displays the body of the response
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
