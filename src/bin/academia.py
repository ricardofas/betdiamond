#!/bin/python

from lxml import html
import requests
import time

file = open('bets.txt','a')
file.write("%s \n" % (time.strftime("%d/%m/%Y")))

page = requests.get('https://www.academiadasapostas.com')
tree = html.fromstring(page.content)

tips_links = tree.xpath('//td[@class="tips"]//a/@href')

for links in tips_links:
	page2 = requests.get(links)
	tree2 = html.fromstring(page2.content)
	match = tree2.xpath('//div[@class="stats-game-head"]/h1/text()')
	bet = tree2.xpath('//div[@class="preview_bet"]/text()')
	odd = tree2.xpath('//span[@class="preview_odd"]/text()')
	if odd:
		string= " | ".join((match[0].strip().encode("utf-8"), bet[0].strip().encode("utf-8"),odd[0].strip().encode("utf-8")))
		file.write("%s\n" % string)

file.close()

