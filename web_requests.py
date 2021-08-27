#!/usr/bin/env python3

import requests
response = requests.get('https://www.google.com')
#response.raise_for_status()
print(response.request.headers['Accept-Encoding'])
print(response.request.headers)
print(response.ok)
print(response.status_code)


p = {"q": "grey kitten",
     "max_results": 15}
response = requests.get("http://www.google.com/search", params=p)
#response.request.url
with open("google_results.html","w") as f:
	f.write(response.text)


p = {"q": "white kitten",
     }
response = requests.post("http://www.google.com/search", data=p)
print(response.request.body)
#with open("google_results_post.html","w") as f:
#	f.write(response.text)


