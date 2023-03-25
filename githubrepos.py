import requests
import json
import sys


def repos(user):
    url = "https://api.github.com/users/{}/repos".format(user)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(
            "HTTP Error: {}.\nAccess: https://http.cat/ for more information".format(
                response.status_code
            )
        )
        return None


username = sys.argv[1]
user_repos = repos(username)
if user_repos is None:
    print("Repo not found!")
else:
    for repo in user_repos:
        print(repo["name"])
        print(repo["html_url"])
