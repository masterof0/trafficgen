#! /usr/bin/env python3

import random, requests, time

groups = ("Social", "Normal", "Marketing", "Tech", "Gamers", "Dev", "Sales", "Streaming", "Sports", "IOC")

while True:
	group = random.choice(groups)
	urls = getattr(__import__('urls', fromlist=[group]), group)

	for url in urls:
		try:
			r=requests.get(url)
			print(url, r.status_code)
		except:
			pass

	time.sleep(random.randint(120,300))
