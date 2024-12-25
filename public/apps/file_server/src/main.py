from pathlib import Path

from fastapi import FastAPI, HTTPException
from markdown import markdown
from enum import Enum

from fastapi.responses import HTMLResponse

app = FastAPI()


class SubFolder(str, Enum):
    BLOG = "blog"


response_mapping = {
    SubFolder.BLOG: HTMLResponse
}


@app.get("/{subfolder}/{path:path}")
async def root(subfolder: SubFolder, path: Path):
    file_path = Path(subfolder.value) / path

    if not file_path.exists():
        raise HTTPException(status_code=404)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        response_type = response_mapping[subfolder]
        return response_type(markdown(content))
