from requests_html import HTMLSession

session = HTMLSession()
response = session.get('https://hn.algolia.com/?q=sql')
if response.status_code == 200:
	response.html.render(sleep = 2)
	titles = response.html.find('article > div')
else:
	print("HTTP Error: {}. Can't get response!!!".format(response.status_code))
i = 1
for title in titles:
	n = title.text.index('\n')
	print(i, title.text[:n])
	i += 1