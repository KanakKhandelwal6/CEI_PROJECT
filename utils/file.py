import json
import os
def save_raw_data(data,filename):
    os.makedirs(os.path.dirname(filename),exist_ok = True)
    with open(filename,"w",encoding="utf-8")as file:
        json.dump(data,file,indent=4)
    


def load_json():
    pass

