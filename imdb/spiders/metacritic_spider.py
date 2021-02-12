# -*- coding: utf-8 -*-
from scrapy import Spider
from metacritic.items import MetaCriticItem


class MetaCriticItem(Spider):
	name = 'metacritic_spider'
	allowed_urls = ['https://www.metacritic.com/']
	start_urls = ['https://www.metacritic.com/browse/movies/score/metascore/all/filtered']

	def parse(self, response):
		# Find all the table rows
		rows = response.xpath('//*[@id="main_content"]/div//table/tbody/tr')
		
		for row in rows:
		
			title = row.xpath('./td[2]/a/h3/text()').extract_first()
			rank = row.xpath('//span[@class="title numbered"/text()').extract_first().strip().replace(".","")

			year = row.xpath('./td[2]/div[2]/span/text()').extract_first()
			rating = row.xpath('//div[@class="clamp-metascore"]/a/text()').extract_first()


			# Initialize a new MetaCriticItem instance for each movie.
			item = MetaCriticItem()
			item['title'] = film
			item['year'] = year
			item['rank'] = awards
			item['rating'] = nominations
			yield item
