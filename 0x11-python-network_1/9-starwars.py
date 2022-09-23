#!/usr/bin/python3
"""
Use requests package to make a get request to the swapi api.
Use string argument as search value of request. Body response must
be JSON and formatted to a Python dictionary.
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.get("https://swapi.co/api/people", params={'search':argv[1]})
    people = r.json()
    print("Number of result: {}".format(people.get('count'])))
    for person in people.get('results'):
        print(person.get('name'))
