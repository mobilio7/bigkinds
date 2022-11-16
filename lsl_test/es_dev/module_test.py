# %%
from newsml_to_json import make_json

xml_dir = '../data'
xml_name = '01100201.20200101000125001.xml'

json_data = make_json(xml_dir, xml_name)
print(json_data)
