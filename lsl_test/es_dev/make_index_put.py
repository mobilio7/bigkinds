# # %%
# import pymysql
# from datetime import datetime as dt

# # now = dt.now()
# # print(now)

# # con = pymysql.connect(host='localhost', user='user', password='lab13579',
# #                        db='NEWSDB', charset='utf8') # 한글처리 (charset = 'utf8')
# # cur = con.cursor()

# # sql = """
# #     SELECT news_id, make_date, provider_id , date_format(provide_date, '%Y-%m-%d') AS provide_date 
# #     from tb_test_news_id
# #     WHERE date_format(make_date, '%Y-%m-%d') BETWEEN '2022-11-10' AND '2022-11-16'
# # """
# # cur.execute(sql)
 
# # rows = cur.fetchall()
# # con.close()
# # print(rows)

# testFile = open('./server.log','rt')

# fileLines = testFile.readlines()
# for line in fileLines:
#     print(line)

# testFile.close()

# # %%
# import pymysql
# import glob
# from newsml_to_json import make_json

# # %%
# # mysql 연결 및 등록된 id list 가져오기
# con = pymysql.connect(host='localhost', user='user', password='lab13579',
#                        db='NEWSDB', charset='utf8') # 한글처리 (charset = 'utf8')
# cur = con.cursor()

# sql = """
#     SELECT news_id, date_format(provide_date, '%Y-%m-%d') 
#     from tb_test_news_id
# """
# cur.execute(sql)
 
# rows = cur.fetchall()
# con.close()
# print(rows)
# # %%
# # 실제 서버 경로
# # rootdir = '/hadoop/newsml/data'
# rootdir = '../data'
# file_arr = []
# for path in glob.glob(f'{rootdir}/*/*/*/*/*'):
#     file_arr.append(path)

# dict_arr = []

# for file in file_arr:
#     file_path = file.split('/')
#     xml_name = file_path[len(file_path)-1]
#     xml_dict = {'news_id':xml_name.replace(".xml",""), 'path':file}
#     dict_arr.append(xml_dict)
# print(dict_arr)

# %%
import pymysql
from datetime import datetime as dt

now = dt.now()
now = str(now)[:10]

# DB 연결
con = pymysql.connect(host='localhost', user='user', password='lab13579'
    ,db='NEWSDB', charset='utf8') # 한글처리 (charset = 'utf8')
# cursor 생성
cur = con.cursor()

# 쿼리 실행
sql = """
    SELECT news_id, make_date, provider_id , date_format(provide_date, '%Y-%m-%d') AS provide_date 
    from tb_test_news_id
    WHERE date_format(make_date, '%Y-%m-%d') BETWEEN %s AND %s
"""
cur.execute(sql, (now, now))
rows = cur.fetchall()
con.close()

print(rows)