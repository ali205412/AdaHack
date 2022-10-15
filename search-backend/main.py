from typing import Dict, List
from starlette.responses import StreamingResponse
from fastapi import FastAPI
import difflib
import yaml

import utils

app = FastAPI()
preprocess_dict = utils.preprocessing()

# threshold for searching
THRESHOLD = 0.9

# search by keyword
@app.get("/search")
async def search(keyword: str) -> List:
    result = []
    for i in preprocess_dict['name_and_descriptions']:
        # change ratio()k -> quick_ratio() if too slow
        if difflib.SequenceMatcher(None, keyword, i).ratio() > THRESHOLD:
            result.append(i)
    return result


# get image from a map
@app.get("/getMap")
async def get_map(name: str) -> StreamingResponse:
    result = None
    try:
        result = StreamingResponse(utils.draw_map(f'./data/Data/{name}/map.csv'), media_type='image/jpg')
    except:
        pass
    return result

@app.get("/getAll")
async def get_all():
    return preprocess_dict['name']

@app.get("/getEUSAMeta")
async def get_eusa_meta(name: str):
    result = None
    try:
        with open(f'./data/Data/{name}/eufs_metadata.yaml') as f:
            result = yaml.safe_load(f)
    except:
        pass
    return result

@app.get("/getMeta")
async def get_meta(name: str):
    result = None
    try:
        with open(f'./data/Data/{name}/metadata.yaml') as f:
            result = yaml.safe_load(f)
    except:
        pass
    return result

@app.get("/debug/preprocess_list")
async def ppl() -> Dict:
    return preprocess_dict
