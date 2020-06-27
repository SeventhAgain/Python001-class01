# -*- coding: utf-8 -*-
import scrapy

from scrapy.selector import Selector

from spiders.items import SpidersItem


class MoviesSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # 翻页url: https://maoyan.com/films?showType=3&offset=90
    # def parse(self, response):
    #     pass

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        for i in range(0, 1):
            url = f'https://maoyan.com/films?showType=3&offset={i * 30}'
            yield scrapy.Request(url=url, callback=self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):

        print(response.url)
        item = SpidersItem()

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
