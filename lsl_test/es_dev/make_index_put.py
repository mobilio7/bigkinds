# %%
import pymysql
import glob
from newsml_to_json import make_json

# %%
# mysql 연결 및 등록된 id list 가져오기
con = pymysql.connect(host='localhost', user='user', password='lab13579',
                       db='NEWSDB', charset='utf8') # 한글처리 (charset = 'utf8')
cur = con.cursor()

sql = """
    SELECT news_id, date_format(provide_date, '%Y-%m-%d') 
    from tb_test_news_id
"""
cur.execute(sql)
 
rows = cur.fetchall()
con.close()
print(rows)
# %%
# 실제 서버 경로
# rootdir = '/hadoop/newsml/data'
rootdir = '../data'
file_arr = []
for path in glob.glob(f'{rootdir}/*/*/*/*/*'):
    file_arr.append(path)

dict_arr = []

for file in file_arr:
    file_path = file.split('/')
    xml_name = file_path[len(file_path)-1]
    xml_dict = {'news_id':xml_name.replace(".xml",""), 'path':file}
    dict_arr.append(xml_dict)
print(dict_arr)

