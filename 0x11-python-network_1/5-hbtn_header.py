#!/usr/bin/python3
"""
Use requests package to make a get request to given URL and display
the value of `X-Request-Id` in response header.
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
