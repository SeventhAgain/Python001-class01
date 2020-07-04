# -*- coding: utf-8 -*-
import scrapy

from scrapy.selector import Selector

from spiders.items import SpidersItem


class MoviesSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3&offset=0'
        yield scrapy.Request(url=url, callback=self.parse)

    # 解析函数
    def parse(self, response):
        item = SpidersItem()
        print(response.url)
        try:
            movies = Selector(response=response).xpath("//div[@class='movie-item-hover']")
            count = 10
            for movie in movies:
                if count > 0:
                    name = movie.xpath('./a/img/@alt')
                    movie_name = name.extract_first()
                    time = movie.xpath('./a/div/div[@class="movie-hover-title movie-hover-brief"]/text()').extract()
                    release_time = time[1].strip()
                    tag_list = movie.xpath("./a/div/div[@class='movie-hover-title']/text()").extract()
                    movie_type = tag_list[4].strip()
                    item['title'] = movie_name
                    item['category'] = movie_type
                    item['date'] = release_time
                    count -= 1
                    yield item
        except Exception as e:
            self.logger.error(e)
