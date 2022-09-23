#!/usr/bin/python3
"""
Use requests package to make a post request sending email param
and display body of response.
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    payload = {'email': sys.argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
