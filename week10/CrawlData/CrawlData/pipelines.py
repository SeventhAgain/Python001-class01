# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import uuid
import re
import datetime

class CrawldataPipeline:


    def process_item(self, item, spider):

        title = item['title']
        link = item['link']
        price = item['price']
        zhi = item['zhi']
        buzhi = item['buzhi']
        collectcount = item['collectcount']
        commentcount = item['commentcount']
        platform = item['platform']
        publish = item['publish']
        comments = item['comments']

        pid = str(uuid.uuid1())

        # 获得产品信息对象
        product_values = (title,link,price,zhi,buzhi,collectcount,commentcount,platform,publish,pid)

        # 获得评论信息列表
        comment_values = (str(comments),pid)

        print(f"产品信息：{product_values}")
        print(f"评论信息：{comment_values}")

        if price != 'None' and zhi != 'None' and buzhi != 'None' and collectcount != 'None' and commentcount != 'None':
            try:
                conn = pymysql.connect(host='192.168.111.130',
                                       port=3306,
                                       user='root',
                                       password='123456',
                                       database='db1',
                                       charset='utf8mb4'
                                       )
                # 获得cursor游标对象
                con_cursor = conn.cursor()

                # 执行插入产品数据
                if product_values:
                    con_cursor.execute('INSERT INTO ' +
                                       'zdm_product(title,link,price,zhi,buzhi,collectcount,commentcount,platform,publish,pid)'
                                       + ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                       product_values)

                # 执行插入评论数据
                if comment_values:
                    con_cursor.execute('INSERT INTO ' +
                                       'zdm_comment(comments,pid)' +
                                       ' values(%s,%s)',
                                       comment_values)

                conn.commit()
                con_cursor.close()
                conn.close()
            except Exception as e:
                # 输出异常信息
                print(e)


