import requests
import json
import sys
import html


def get_QA(label):
    url = "https://api.stackexchange.com/2.3/questions?order=desc&sort=votes&tagged={}&site=stackoverflow"
    response = requests.get(url.format(label))
    if response.status_code == 200:
        return response.json()
    else:
        print(
            "HTTP Error: {}.\nAccess: https://http.cat/ for more information".format(
                response.status_code
            )
        )
        return None


n = sys.argv[1]
label = sys.argv[2]
questions = get_QA(label)
if questions is None:
    print("No Quetion Found")
else:
    for question in questions["items"][: int(n)]:
        print(html.unescape(question["title"]))
        print(question["link"] + "\n")
