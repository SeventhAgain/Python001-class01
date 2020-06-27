# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd


class SpidersPipeline(object):
    def process_item(self, item, spider):

        # mode='a'是代表追加数据，不覆盖
        data = [item['title'],item['category'],item['date']]
        columns=['name','category','date']
        pd.DataFrame(columns=columns,data=[data]).to_csv('./maoyan.csv', encoding='utf8', index=False, mode='a', header=False)
        return item
