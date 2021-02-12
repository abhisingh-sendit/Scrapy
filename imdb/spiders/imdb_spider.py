# -*- coding: utf-8 -*-
from scrapy import Spider
from imdb.items import WikiItem


class ImdbSpider(Spider):
	name = 'imdb_spider'
	allowed_urls = ['https://www.imdb.com/']
	start_urls = ['https://www.imdb.com/chart/top/']

	def parse(self, response):
		# Find all the table rows
		rows = response.xpath('//*[@class="lister"]/div/table/tbody/tr')
		
		for row in rows:
			title = row.xpath('./td[2]/a/text()').extract_first()
			year = row.xpath('//span[@class="secondaryInfo"/text()').extract_first().strip()

			rank = row.xpath('./text()').extract_first().strip().replace(".","")
			rating = row.xpath('./td[3]/strong/text()').extract_first().strip()



			# Initialize a new ImdbItem instance for each movie.
			item = ImdbItem()
			item['title'] = title
			item['year'] = year
			item['rank'] = rank
			item['rating'] = rating
			yield item
