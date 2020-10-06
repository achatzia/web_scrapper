#!/usr/bin/env python

import sys, requests, csv
from bs4 import BeautifulSoup

var = sys.argv[1]


source = requests.get("https://www.oneman.gr/" + str(var) + "/").text
soup = BeautifulSoup(source, 'lxml')
def rss_feed(var):
	with open('rss_feed.csv', "w") as rss_feed_csv:
		writer = csv.writer(rss_feed_csv)
		writer.writerow(['headline', 'summary', 'link_to'])
		for article in soup.find_all('article'):
			headline = article.h3.a.text.strip().upper()
			print("Article Headline: {}\n".format(headline))
			summary = article.find('div', class_='article__lead').p.text
			print("Article Summary : {}\n".format(summary))
			try:
				link_to = article.find('h3', class_='post__title').a['href']
			except Exception as e:
				print("Link not found")
			print("Link to Article : {}\n".format(link_to))
			writer.writerow([headline, summary, link_to])
	rss_feed_csv.close()


rss_feed(var)
