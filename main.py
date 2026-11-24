from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from db import init_db, save_url, get_url
from encoder import encode, decode
from pydantic import BaseModel

app = FastAPI()
init_db()

@app.get("/health")
def health():
    return {"status": "ok"}


class ShortenReq(BaseModel):
    long_url: str


@app.post("/shorten")
def shorten(request: ShortenReq): # direct to use the class
    get_id = save_url(request.long_url)
    code = encode(get_id)

    return {"code": code, "short_url": f"http://127.0.0.1:8000/{code}"}


@app.get("/{code}")
def code_getter(code: str):
    try:
        get_id = decode(code)
    except ValueError:
        raise HTTPException(status_code=404, detail="Short link not found.")

    long_url = get_url(get_id)
    if long_url is None:
        raise HTTPException(status_code=404, detail="Short link not found.")

    return RedirectResponse(long_url)

    
