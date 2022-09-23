#!/usr/bin/python3
"""
Take in a URL and email, send POST request, and display body of response
decoded in utf-8
"""
if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as r:
        print(r.read().decode('utf-8'))
