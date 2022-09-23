#!/usr/bin/python3
"""
Take in a URL, send a request to URL, and dispaly body of response decoded in
utf-8. Manage urllib's error exceptions.
"""
if __name__ == "__main__":
    import urllib.error as Error
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
