from typing import Dict

from fastapi import FastAPI
import difflib

import utils

app = FastAPI()

preprocess_dict = utils.preprocessing()
THRESHOLD = 0.9

print(preprocess_dict)

@app.get("/search")
async def search(keyword: str):
    result = []
    for i in preprocess_dict['name_and_descriptions']:
        # change ratio()k -> quick_ratio() if too slow
        if difflib.SequenceMatcher(None, keyword, i).ratio() > THRESHOLD:
            result.append(i)
    return result



@app.get()

@app.get("/debug/preprocess_list")
async def ppl() -> Dict:
    return preprocess_dict
