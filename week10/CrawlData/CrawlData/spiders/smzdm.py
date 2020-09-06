# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

from CrawlData.items import CrawldataItem


class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['smzdm.com']
    start_urls = ['http://smzdm.com/']

    # https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p5/

    # 评论自动翻页
    def get_comment_page(self, pstr):
        if pstr ==  'None':
            return 0;
        m = int(pstr)
        result = int(0)
        if m == 0:
            pass
        else:
            mod = m % 30
            quote = m // 30
            if mod > 0:
                quote = quote + 1
            result = quote
        return result

    def start_requests(self):
        for i in range(1, 45):
            url = f'https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p{i}'
            yield scrapy.Request(url=url, callback=self.parse_list)

    # 处理列表页
    def parse_list(self, response):
        print(f'url:{response.url}')

        # 分析列表中每一个产品
        products = Selector(response=response).xpath('//li[@class="feed-row-wide"]')

        if products:
            for product in products:
                title = product.xpath('./div/div[2]/h5/a/text()')
                link = product.xpath('./div/div[2]/h5/a/@href')
                # 价格
                price = product.xpath('./div/div[2]/div[1]/a/text()')
                # 值数量
                zhi = product.xpath('./div/div[2]/div[3]/div[1]/span/a[1]/span[1]/span/text()')
                # 不值数量
                buzhi = product.xpath('./div/div[2]/div[3]/div[1]/span/a[2]/span[1]/span/text()')
                # 收藏数量
                collectcount = product.xpath('./div/div[2]/div[3]/div[1]/a[1]/span/text()')
                # 评论数量
                commentcount = product.xpath('./div/div[2]/div[3]/div[1]/a[2]/span/text()')
                # 平台
                platform = product.xpath('./div/div[2]/div[3]/div[2]/span/a/text()')
                # 发布时间
                publish = product.xpath('./div/div[2]/div[3]/div[2]/span/text()')

                productitem = CrawldataItem()
                productitem['title'] = str(title.extract_first()).strip('\n').strip()
                productitem['link'] = str(link.extract_first()).strip('\n').strip()
                productitem['price'] = str(price.extract_first()).strip('\n').strip()
                productitem['zhi'] = str(zhi.extract_first()).strip('\n').strip()
                productitem['buzhi'] = str(buzhi.extract_first()).strip('\n').strip()
                productitem['collectcount'] = str(collectcount.extract_first()).strip('\n').strip()
                productitem['commentcount'] = str(commentcount.extract_first()).strip('\n').strip()
                productitem['platform'] = str(platform.extract_first()).strip('\n').strip()
                productitem['publish'] = str(publish.extract_first()).strip('\n').strip()

                # 实现评论翻页功能（思路：每页最多30个评论，根据评论数推断评论页数）
                page_count = self.get_comment_page(productitem['commentcount'])
                if page_count > 0:
                    for i in range(1, page_count + 1):
                        url = f'{link.extract()[0]}/p{i}/#comments'
                        print(f'评论分页url：{url}')
                        yield scrapy.Request(url=url, meta={'item': productitem}, callback=self.parse_details)
                else:
                    productitem['comments'] = ''
                    yield productitem

    # 处理详情页
    def parse_details(self, response):

        # 开始评论详情
        print(response.url)
        details = Selector(response=response).xpath('//li[@class="comment_list"]')
        productitem = response.meta['item']
        mlist = []
        if details:
            for detail in details:
                publisher = str(detail.xpath('./div[2]/div[1]/a/span/text()').extract_first().strip('\n').strip())
                datePublished = str(
                    detail.xpath('./div[2]/div[1]/div[1]/meta/@content').extract_first().strip('\n').strip())
                timePublished = str(detail.xpath('./div[2]/div[1]/div[1]/text()').extract_first().strip('\n').strip())
                comment = str(detail.xpath(
                    './div[2]/div[3]/div[1]/p/span/text() | ./div[2]/div[2]/div[1]/p/span/text()').extract_first().strip(
                    '\n').strip())
                dict = {'publisher': publisher, 'datePublished': datePublished,
                        'timePublished': timePublished, 'comment': comment}
                mlist.append(dict)
        productitem['comments'] = mlist
        yield productitem



