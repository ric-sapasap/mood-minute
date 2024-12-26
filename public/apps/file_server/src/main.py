import json
import os
from pathlib import Path

import yaml
from fastapi import FastAPI, HTTPException
from markdown import markdown
from enum import Enum

from fastapi.responses import HTMLResponse, JSONResponse
from mnemonic import Mnemonic

app = FastAPI()


class SubPath(str, Enum):
    IDENTITY = "id"
    BLOG = "blog"
    API = "api"


response_mapping = {
    SubPath.IDENTITY: JSONResponse,
    SubPath.BLOG: HTMLResponse,
    SubPath.API: JSONResponse,
}


@app.get("/id")
async def identity():
    print(os.curdir)
    with open("IDENTITY", "r", encoding="utf-8") as f:
        content_dict = yaml.safe_load(f)
        return JSONResponse(content_dict)


@app.get("/api/mnemonic/generate")
async def generate_mnemonic():
    mnemo = Mnemonic("english")
    words = mnemo.generate(strength=256)
    return JSONResponse(
        {
            "identity.json": words.split()
        }
    )


@app.get("/blog/{path:path}")
async def blog(path: Path):
    file_path = Path("blog") / path

    if not file_path.exists():
        raise HTTPException(status_code=404)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        return HTMLResponse(markdown(content))
