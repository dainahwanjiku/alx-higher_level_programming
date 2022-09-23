#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
Arguments: arg1: repo name, arg2: repo owner
"""
if __name__ == "__main__":
    from sys import argv
    import requests
    # Get the arguments, arg1: repo name, arg2: repo owner
    url = requests.get("https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1]))
    commits = r.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=':')
        print(commit.get('commit').get('author').get('name'))
