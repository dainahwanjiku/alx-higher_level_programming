#!/usr/bin/python3
"""
Use requests package to make a get request to given URL and display
the body of response, or error code if error.
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.get(argv[1])
    try:
        r.raise_for_status()
        print(r.text)
    except Exception as e:
        print("Error code: {}".format(r.status_code))
