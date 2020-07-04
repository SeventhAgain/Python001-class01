# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class SpidersPipeline:

    def __init__(self):
        conn = pymysql.connect(
            host='192.168.111.130',
            port=3306,
            user='root',
            password='123456',
            db='test'
        )
        self.conn = conn

    def process_item(self, item, spider):

        try:
            sql = "insert into maoyan(name,type,date) values (%s,%s,%s)"
            values = (item['title'],item['category'],item['date'])
            print(values)
            self.conn.cursor().execute(sql,values)
            self.conn.commit()
        except:
            self.conn.rollback()

        return item
