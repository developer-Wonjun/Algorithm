import pickle
import json
from numpyencoder.numpyencoder import NumpyEncoder

COLORCHIP_DB = "colorchipDB_json.json"

with open(COLORCHIP_DB, 'rt', encoding='UTF-8') as f:
    colorchips_b = json.load(f)

colorchip = {}

for cur_key in list(colorchips_b.keys()):
    new_line = {}
    for key in list(colorchips_b[cur_key]):
        cur_val = colorchips_b[cur_key][key]

        if type(cur_val) is not list:
            cur_val = cur_val
            
        new_key = key
        new_line[new_key] = cur_val
    colorchip[cur_key] = new_line

with open('data.pickle', 'wb') as f:
    pickle.dump(colorchip, f, pickle.HIGHEST_PROTOCOL)