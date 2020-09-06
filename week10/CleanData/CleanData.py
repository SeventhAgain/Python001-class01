import pandas as pd
from snownlp import SnowNLP
from sqlalchemy import create_engine

# NLP舆情分析函数
def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments

# mysql数据库配置信息
db_info = {'user': 'root',
           'password': '000000',
           'host': '192.168.111.130',
           'port': 3306,
           'database': 'db1'
           }

if __name__ == "__main__":
    # 建立mysql数据库连接
    engine = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)d/%(database)s?charset=utf8' % db_info, encoding='utf-8')

    # 一、处理评论信息
    # 加载评论信息
    sql_comment= 'SELECT *  FROM zdm_comment'
    df_com = pd.read_sql(sql_comment,engine)

    # 处理重复的评论信息
    df_com.drop_duplicates(subset=None, keep='first', inplace=True)

    # 清理评论内容为空值的信息
    df_com.drop(labels = (df_com[df_com['comments'] == ""].index), axis = 0,inplace= True)

    # 为评论信息添加舆情分析判断
    df_com["sentiment"] = df_com.comment.apply(_sentiment)

    # 将清洗后的评论数据存入mysql
    df_com.to_sql('zdm_comment', engine, if_exists='replace', index=False)

    # 将处理完毕的品牌舆情信息存入mysql数据库持久化保存
    m = df_pro_com[['id','datePublished','comments','sentiment','title','platform','publisher']].to_sql('zdm_pro_com', engine, if_exists='replace', index=True)

