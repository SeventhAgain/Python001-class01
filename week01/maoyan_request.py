#  -*- coding:utf-8 -*-

import requests

from bs4 import BeautifulSoup as bs

import lxml.etree

import pandas as pd

# 猫眼电影：https://maoyan.com/
# 即将上映：https://maoyan.com/films?showType=2
# 经典影片: https://maoyan.com/films?showType=3

# 影片详情：https://maoyan.com/films/1250952

base_url = 'https://maoyan.com'

my_url = 'https://maoyan.com/films?showType=3'

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"

cookie = '__mta=244087482.1593009413633.1593058344392.1593058382316.15; uuid_n_v=v1; uuid=2586CDC0B62811EAB4E28FB161D5B82B84117DE8075B44A2A94BBD4F8AE51E72; _lxsdk_cuid=172e6c29b28c8-0e6b445b34f429-5313f6f-240000-172e6c29b28c8; _lxsdk=2586CDC0B62811EAB4E28FB161D5B82B84117DE8075B44A2A94BBD4F8AE51E72; mojo-uuid=0ef0b51398e09066b8358c64a9080026; _csrf=720fb0044af2176efca4c8967e27ded992b007f0fa7c14c4f248c166e2e5e51d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593009413,1593051944; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; mojo-session-id={"id":"cb18a635131bc81a7d4993b293eb0edf","time":1593061170242}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593061171; __mta=244087482.1593009413633.1593058382316.1593061171937.16; _lxsdk_s=172e9d86255-064-03b-599%7C%7C2'

header = {'user-agent': user_agent, 'Cookie': cookie}

response = requests.get(my_url, headers=header)

print(response.url)

bs_info = bs(response.text, 'html.parser')

movies = []

count=10

# 列表页
for tags in bs_info.find_all("div", attrs={'class', 'channel-detail movie-item-title'}):
    if count>0:
        for a_tag in tags.find_all("a"):
            detail_url = base_url+a_tag.get('href');
            detail_response = requests.get(detail_url,headers=header)
            detail_bs_info = bs(detail_response.text,'html.parser')

            # xml化处理
            selector = lxml.etree.HTML(detail_response.text)

            for detail_tags in detail_bs_info.find_all("div",attrs={'class','movie-brief-container'}):
                movie_type = ''
                for name_tag in detail_tags.find_all("h1"):
                    movie_name = name_tag.text
                for type_tag in detail_tags.find_all("a"):
                    movie_type= movie_type+type_tag.text

                # 用一下xpath
                release_time = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
                release_time = "".join(release_time)

                each_movie =[movie_name,movie_type,release_time]
                data = pd.DataFrame(data=each_movie)

                # 追加的方式写入文件
                data.to_csv('./movies.csv', encoding='utf8', mode="a",index=False, header=False)
        count-=1