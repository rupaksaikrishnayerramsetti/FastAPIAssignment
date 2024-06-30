from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI()

@app.get("/")
def read():
    return {"hello": "world"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=9000)