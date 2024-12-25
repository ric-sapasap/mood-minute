from pathlib import Path

from fastapi import FastAPI, HTTPException
from markdown import markdown
from enum import Enum

app = FastAPI()


class SubFolder(str, Enum):
    BLOG = "blog"


@app.get("/{subfolder}/{path:path}")
async def root(subfolder: SubFolder, path: Path):
    file_path = Path(subfolder.value) / path

    if not file_path.exists():
        raise HTTPException(status_code=404)

    with open(file_path, "r") as f:
        content = f.read()
        return {"message": markdown(content)}
