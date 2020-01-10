import random, requests, time

groups = ("Social", "Normal", "Marketing", "Tech", "Gamers", "Dev", "Sales", "Streaming")

while True:
	group = random.choice(groups)
	urls = getattr(__import__('urls', fromlist=[group]), group)

	for url in urls:
		r=requests.get(url)
		print r.status_code	

	time.sleep(random.randint(120,300))
