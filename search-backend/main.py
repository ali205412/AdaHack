from typing import Dict, List
from starlette.responses import StreamingResponse
import difflib
import yaml
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, UploadFile
import os
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
import requests

import utils

app = FastAPI()
templates = Jinja2Templates(directory="templates")
# download file by access ${URI}/data/${FILENAME}
# E.g. 127.0.0.1:8000/data/rosbag2_2022_05_14-16_06_49/rosbag2_2022_05_14-16_06_49.db3.zip

app.mount('/data', StaticFiles(directory="data/Data"), name="data")
preprocess_dict = utils.preprocessing()

# threshold for searching
THRESHOLD = 0.9


# search by keyword
@app.get("/search")
async def search(keyword: str) -> List:
    result = {}
    for i in preprocess_dict['name_and_descriptions']:
        # change ratio()k -> quick_ratio() if too slow
        result[i] = difflib.SequenceMatcher(None, keyword, i).ratio()
    return sorted(result.keys(), key=lambda x: -result[x])[:10]


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


@app.get("/getEUFSMeta")
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


@app.get("/debug")
async def ppl() -> Dict:
    return utils.get_metadata()


# api endpoint for uploading files
@app.post("/uploadFile")
async def create_upload_file(file: UploadFile, name: str):
    path = f'./data/Data/{name}'
    if not os.path.exists(path):
        os.makedirs(path)
    with open(f'{path}/{name}/{file.filename}', mode='wb') as f:
        f.write(file.file.read())

    return {
        "filename": file.filename,
        "location": f'{path}/{name}/{file.filename}'
    }


@app.get("/viewDetail", response_class=HTMLResponse)
def view_detail(request: Request, name: str):
    eufs_meta = ""
    meta = ""
    try:
        with open(f'./data/Data/{name}/eufs_metadata.yaml') as f:
            eufs_meta = f.read()
        with open(f'./data/Data/{name}/metadata.yaml') as f:
            meta = f.read()
        return templates.TemplateResponse("detail.html", {"request": request, "name": name,
                                                          "eufs_meta": eufs_meta, "meta": meta})
    except:
        name = preprocess_dict['desc_to_name'][name]
        with open(f'./data/Data/{name}/eufs_metadata.yaml') as f:
            eufs_meta = f.read()
        with open(f'./data/Data/{name}/metadata.yaml') as f:
            meta = f.read()
        return templates.TemplateResponse("detail.html", {"request": request, "name": name,
                                                          "eufs_meta": eufs_meta, "meta": meta})

@app.get("/searchView", response_class=HTMLResponse)
def search_view(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})