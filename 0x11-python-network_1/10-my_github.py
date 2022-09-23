#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
if __name__ == "__main__":
    import sys
    import requests
    from requests.auth import HTTPBasicAuth
    r = requests.get('https://api.github.com/users/{}'.format(argv[1]),
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))
