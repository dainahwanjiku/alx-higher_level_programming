#!/usr/bin/python3
"""Use requests package to make a get request to given URL
"""
if __name__ == "__main__":
    import requests
    r = requests.get("https://intranet.hbtn.io/status")
    text = r.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
