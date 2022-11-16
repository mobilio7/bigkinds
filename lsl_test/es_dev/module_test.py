# %%
from newsml_to_json import make_json

xml_dir = '..\data'
xml_name = '01100201.20200101000125001.xml'

json_data = make_json(xml_dir, xml_name)
print(json_data)

# %%
import os

# 실제 서버 경로
# dir = '/bitdata/outsource/'
dir = '..\data\outsource'

# file_list = os.listdir(dir)
# for file in file_list:
#     print(file)

for file in os.listdir(dir):
    d = os.path.join(dir, file)
    if os.path.isdir(d):
        print(d)

# %%
# 디렉토리 리스트 뽑고 파일 목록 뽑기
# !!!!! 윈도우라 \ 사용, 리눅스에서는 / 사용햋야함!!!!!!!!!
import glob

rootdir = '..\data\outsource'
path_name = ''
for path in glob.glob(f'{rootdir}/*/*/*/*/*/*'):
    print(path)
    path_name = path

path_arr = path_name.split('\\')
xml_name = path_arr[len(path_arr)-1]
xml_dir = ''
for txt in path_arr:
    if xml_name == txt:
        break
    else :
        xml_dir += txt+'\\'
xml_dir = xml_dir[:-1]

print(xml_dir+"\\"+xml_name)
print(len(xml_name.replace(".xml","")))
# make_json(xml_dir, xml_name)
