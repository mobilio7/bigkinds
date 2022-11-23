import json
import xmltodict

def make_json(xml_dir):
    with open(xml_dir,'r', encoding='utf-8') as f:
        xmlString = f.read()

    jsonDump = xmltodict.parse(xmlString, attr_prefix='', cdata_key='text')

    # json 파일 저장 필요할 경우 사용
    # dir_arr = xml_dir.split('/')
    # xml_name = dir_arr[len(dir_arr)-1]
    # jsonString = json.dumps(jsonDump, indent=4)
    # with open(xml_name.replace(".xml",".json"), 'w') as f:
    #     f.write(jsonString)
    
    return jsonDump