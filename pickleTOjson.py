import pickle
import json
from numpyencoder.numpyencoder import NumpyEncoder

COLORCHIP_DB = "personalColorChips_Live_Add8Chips_20190715.pickle"

handle = open(COLORCHIP_DB, 'rb')
loadPickle = pickle.load(handle, encoding='bytes')

jsonFile = {}

for cur_key in list(loadPickle.keys()):
    new_line = {}
    for key in list(loadPickle[cur_key]):
        cur_val = loadPickle[cur_key][key]

        if type(cur_val) is not list:
            cur_val = cur_val.decode('cp949').encode('utf-8').decode('utf-8')
            
        new_key = key.decode('cp949').encode('utf-8').decode('utf-8') 
        new_line[new_key] = cur_val
    jsonFile[cur_key.decode('cp949').encode('utf-8').decode('utf-8') ] = new_line

with open('colorchipDB_JSON.json', 'w', encoding="utf-8") as make_file:
  make_file.write(json.dumps(jsonFile, cls= NumpyEncoder, indent=4,ensure_ascii=False))
