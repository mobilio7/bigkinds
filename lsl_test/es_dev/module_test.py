# %%
# from newsml_to_json import make_json

# xml_dir = '..\data'
# xml_name = '01100201.20200101000125001.xml'

# json_data = make_json(xml_dir, xml_name)
# print(json_data)

# %%
# import os

# dir = '../data'

# file_list = os.listdir(dir)
# for file in file_list:
#     print(file)

# for file in os.listdir(dir):
#     d = os.path.join(dir, file)
#     if os.path.isdir(d):
#         print(d)

# %%
# 디렉토리 리스트 뽑고 파일 목록 뽑기
# !!!!! 윈도우라 \ 사용, 리눅스에서는 / 사용해야함!!!!!!!!!
import glob
from newsml_to_json import make_json

# 실제 서버 경로
# rootdir = '/hadoop/newsml/data'
rootdir = '../data'
file_arr = []
for path in glob.glob(f'{rootdir}/*/*/*/*/*'):
    file_arr.append(path)

name_arr = []
dir_arr = []

dict_arr = []

for file in file_arr:
    file_path = file.split('/')
    xml_name = file_path[len(file_path)-1]
    xml_dir = ''
    for txt in file_path:
        if xml_name == txt:
            break
        else:
            xml_dir += txt+'/'
    xml_dir = xml_dir[:-1]
    xml_dict = {'name':xml_name, 'path':xml_dir, 'full_path':file}
    dict_arr.append(xml_dict)
    # name_arr.append(xml_name)
    # dir_arr.append(xml_dir)
print(dict_arr)


# print(xml_dir+"/"+xml_name)
# print(xml_name.replace(".xml",""))
# jsondict = make_json(xml_dir, xml_name)

# %%
# STEP 1
import pymysql

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='localhost', user='user', password='lab13579',
                       db='NEWSDB', charset='utf8') # 한글처리 (charset = 'utf8')
 
# STEP 3: Connection 으로부터 Cursor 생성
cur = con.cursor()
 
# STEP 4: SQL문 실행 및 Fetch
sql = """
    SELECT news_id, date_format(provide_date, '%Y-%m-%d') 
    from tb_test_news_id
"""
cur.execute(sql)
 
# 데이타 Fetch
rows = cur.fetchall()
print(rows)     # 전체 rows

# STEP 5: DB 연결 종료
con.close()