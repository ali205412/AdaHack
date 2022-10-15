import os
import yaml
from typing import Dict
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd

def preprocessing() -> Dict:
    base_dir = './data/Data'
    dirs = os.listdir(base_dir)
    name = []
    descriptions = []
    desc_to_name = {}
    for i in dirs:
        name.append(i)
        try:
            with open(f'{base_dir}/{i}/eufs_metadata.yaml', mode='r') as f:
                data = yaml.safe_load(f)
            desc = data['description']
            descriptions.append(desc)
            desc_to_name[desc] = i
        except:
            pass
    name_and_descriptions = name + descriptions
    return {
        'name': name,
        'name_and_descriptions': name_and_descriptions,
        'descriptions': descriptions,
        "desc_to_name": desc_to_name
    }


def draw_map(file_address: str) -> str:
    df = pd.read_csv(file_address)
    for i in ['blue', 'yellow', 'orange', 'big_orange']:
        c = i
        sz = 30
        if c == 'big_orange':
            c = 'orange'
            sz = 100
        plt.scatter(df['x'][df['cone_type'] == i], df['y'][df['cone_type'] == i], color=c, s=sz, edgecolors='black')
    my_stringIObytes = io.BytesIO()
    plt.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    return my_stringIObytes
