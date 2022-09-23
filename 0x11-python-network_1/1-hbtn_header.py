#!/usr/bin/python3
"""
Take in a URL, send request to URL and display value of `X-Request-Id`
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    with request.urlopen(sys.argv[1]) as res:
        print(res.info()['X-Request-Id'])
