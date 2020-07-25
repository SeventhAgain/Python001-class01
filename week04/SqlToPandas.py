# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
df.columns = ['no', 'name', 'age', 'character', 'motto']

# case1
print("SELECT * FROM data;")
print(df)
print("\n")

# case2
print("SELECT * FROM data LIMIT 10")
print(df[0:10])
print("\n")

# case3
print("SELECT name FROM data;")
print(df['name'])
print("\n")

# case4
print("SELECT COUNT(name) FROM data;")
print(df['name'].count())
print("\n")

# case5
print("SELECT * FROM data WHERE no>6 AND age<=30")
print(df[(df['no'] > 6) & (df['age'] <= 30)])
print("\n")

# case6
print("SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;")
df2 = pd.DataFrame([
    {'id': '10010', 'name': 'xiaoming', 'order_id': '11111'},
    {'id': '10010', 'name': 'xiaohong', 'order_id': '11111'},
    {'id': '10010', 'name': 'xiaoqiang', 'order_id': '11112'},
    {'id': '10011', 'name': 'xiaoli', 'order_id': '11112'},
    {'id': '10011', 'name': 'xiaowang', 'order_id': '11113'},
    {'id': '10011', 'name': 'xiaozhao', 'order_id': '11113'}
])
print(df2.groupby('id').aggregate({'order_id': 'nunique'}))
print("\n")

# case7
print("SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;")
group = ['a', 'b', 'c']
table1 = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 10)],
    "age": np.random.randint(15, 50, 10)
})

table2 = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 10)],
    "salary": np.random.randint(5, 50, 10),
})
print(pd.merge(table1, table2, on='group', how='inner'))

# case8
print("SELECT * FROM table1 UNION SELECT * FROM table2;")
print(pd.concat([table1, table2]).drop_duplicates())

# case9
print("DELETE FROM table1 WHERE id=10;")
delete_index = df[df['no'] == 10].index
print(df.drop(delete_index, axis=0))

# case 10
print("ALTER TABLE table1 DROP COLUMN column_name;")
print(df.drop('no', axis=1))
