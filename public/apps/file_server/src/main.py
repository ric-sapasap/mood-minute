from pathlib import Path

from fastapi import FastAPI, HTTPException
from markdown import markdown
from enum import Enum

from fastapi.responses import HTMLResponse, JSONResponse
from mnemonic import Mnemonic

app = FastAPI()


class SubPath(str, Enum):
    BLOG = "blog"
    API = "api"


response_mapping = {
    SubPath.BLOG: HTMLResponse,
    SubPath.API: JSONResponse
}


@app.get("/blog/{path:path}")
async def blog(path: Path):
    file_path = Path("blog") / path

    if not file_path.exists():
        raise HTTPException(status_code=404)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        return HTMLResponse(markdown(content))


@app.get("/api/mnemonic/generate")
async def generate_mnemonic():
    mnemo = Mnemonic("english")
    words = mnemo.generate(strength=256)
    return JSONResponse(
        {
            "identity.json": words.split()
        }
    )
