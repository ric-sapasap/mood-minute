from pathlib import Path

from fastapi import FastAPI

app = FastAPI()


@app.get("/{path:path}")
async def root(path: Path):
    return {"message": f"{path}"}
